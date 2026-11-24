/**
 * AppDirectory International Fuzzy Search Engine
 * Features:
 * - Full Unicode and diacritic normalization (NFD)
 * - Typo tolerance with Damerau-Levenshtein distance & transpositions
 * - Single-letter and partial prefix matching
 * - Subsequence and abbreviation matching (e.g., 'vsc' -> VSCodium, '7z' -> 7-Zip)
 * - Multi-token querying with field-weighted relevance scoring
 * - Keyword and synonym expansion
 * - URL query string synchronization (?q=...)
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.AppSearchEngine = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {

  // Unicode Diacritic & Punctuation Normalization
  function normalizeText(text) {
    if (!text) return '';
    return text
      .toString()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '') // remove accent marks
      .toLowerCase()
      .replace(/['"’`]/g, '')           // remove quotes
      .replace(/[^\w\s\-\+\.]/g, ' ')   // clean punctuation into spaces
      .trim()
      .replace(/\s+/g, ' ');
  }

  // Damerau-Levenshtein Distance (handles insertions, deletions, substitutions, transpositions)
  function damerauLevenshtein(a, b) {
    if (a === b) return 0;
    const lenA = a.length;
    const lenB = b.length;
    if (lenA === 0) return lenB;
    if (lenB === 0) return lenA;

    // Fast-path length discrepancy
    if (Math.abs(lenA - lenB) > 3) return 99;

    const d = [];
    for (let i = 0; i <= lenA; i++) {
      d[i] = [i];
    }
    for (let j = 0; j <= lenB; j++) {
      d[0][j] = j;
    }

    for (let i = 1; i <= lenA; i++) {
      for (let j = 1; j <= lenB; j++) {
        const cost = a[i - 1] === b[j - 1] ? 0 : 1;
        d[i][j] = Math.min(
          d[i - 1][j] + 1,       // deletion
          d[i][j - 1] + 1,       // insertion
          d[i - 1][j - 1] + cost // substitution
        );

        // Transposition
        if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) {
          d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
        }
      }
    }

    return d[lenA][lenB];
  }

  // Subsequence Check (e.g., 'vsc' matches 'vscodium', '7z' matches '7-zip')
  function isSubsequence(query, target) {
    if (!query || !target) return false;
    let qIdx = 0;
    for (let tIdx = 0; tIdx < target.length && qIdx < query.length; tIdx++) {
      if (query[qIdx] === target[tIdx]) {
        qIdx++;
      }
    }
    return qIdx === query.length;
  }

  // Match a single query token against a candidate word
  function scoreTokenAgainstWord(token, word) {
    if (!token || !word) return 0;
    if (token === word) return 100;

    // Prefix match
    if (word.startsWith(token)) {
      if (token.length === 1) return 85;
      return 92;
    }

    // Substring match
    if (word.includes(token)) {
      return 80;
    }

    // Subsequence match (for acronyms/abbreviations)
    if (token.length >= 2 && isSubsequence(token, word)) {
      return 72;
    }

    // Typo Tolerance / Fuzzy Match via Damerau-Levenshtein
    const tLen = token.length;
    const wLen = word.length;

    // For short tokens (<= 2 chars), don't allow fuzzy typos to prevent false positives
    if (tLen <= 2) return 0;

    const maxDistance = tLen >= 7 ? 2 : (tLen >= 4 ? 1 : 1);
    const dist = damerauLevenshtein(token, word);

    if (dist <= maxDistance) {
      // Score decreases with distance and relative word length
      const penalty = dist * 18;
      return Math.max(50, 75 - penalty);
    }

    return 0;
  }

  // Tokenize and clean text into searchable words
  function tokenize(text) {
    const clean = normalizeText(text);
    return clean ? clean.split(/\s+/).filter(Boolean) : [];
  }

  /**
   * Search an item with weighted fields
   * @param {Object} item Candidate object
   * @param {Array} queryTokens Array of normalized query tokens
   */
  function scoreItem(item, queryTokens) {
    if (!queryTokens.length) return 1;

    // Define weighted field contents
    const fields = [
      { text: item.name || '', weight: 3.5 },
      { text: (item.keywords || []).join(' '), weight: 3.0 },
      { text: item.badge || '', weight: 2.5 },
      { text: item.category || '', weight: 2.2 },
      { text: item.desc || '', weight: 1.5 },
      { text: item.fullDesc || '', weight: 1.0 },
      { text: item.platform || '', weight: 1.0 }
    ];

    // Pre-tokenize item fields
    const tokenizedFields = fields.map(f => ({
      tokens: tokenize(f.text),
      rawText: normalizeText(f.text),
      weight: f.weight
    }));

    let totalScore = 0;

    // Every query token must match AT LEAST ONE field in the item
    for (const qToken of queryTokens) {
      let maxTokenScore = 0;

      for (const field of tokenizedFields) {
        // Direct phrase/substring match on full field string
        if (field.rawText.includes(qToken)) {
          const directScore = (qToken === field.rawText ? 100 : 85) * field.weight;
          if (directScore > maxTokenScore) maxTokenScore = directScore;
        }

        // Word-level token match with fuzzy/typo tolerance
        for (const wToken of field.tokens) {
          const wordScore = scoreTokenAgainstWord(qToken, wToken) * field.weight;
          if (wordScore > maxTokenScore) {
            maxTokenScore = wordScore;
          }
        }
      }

      // If any query token fails completely, this item is not a match
      if (maxTokenScore === 0) {
        return 0;
      }

      totalScore += maxTokenScore;
    }

    return totalScore;
  }

  // App Search Engine Class
  class AppSearchEngine {
    constructor(items, options = {}) {
      this.items = items || [];
      this.options = Object.assign({
        threshold: 30,
        sort: true
      }, options);
    }

    search(query, categoryFilter = 'all') {
      const normalizedQuery = normalizeText(query);
      const queryTokens = normalizedQuery ? normalizedQuery.split(/\s+/).filter(Boolean) : [];

      const results = [];

      for (let i = 0; i < this.items.length; i++) {
        const item = this.items[i];

        // Category filter check
        if (categoryFilter && categoryFilter.toLowerCase() !== 'all') {
          if (!item.category || item.category.toLowerCase() !== categoryFilter.toLowerCase()) {
            continue;
          }
        }

        // If no query string, all category-matching items are returned
        if (!queryTokens.length) {
          results.push({ item, score: 100, index: i });
          continue;
        }

        const score = scoreItem(item, queryTokens);
        if (score >= this.options.threshold) {
          results.push({ item, score, index: i });
        }
      }

      // Sort by score descending, preserving index order for ties
      if (this.options.sort) {
        results.sort((a, b) => b.score - a.score || a.index - b.index);
      }

      return results.map(r => r.item);
    }

    // Helper: Sync search query with URL parameter without reloading
    static syncUrlQuery(query) {
      if (typeof window === 'undefined' || !window.history || !window.location) return;
      try {
        const url = new URL(window.location.href);
        const trimmed = (query || '').trim();
        if (trimmed) {
          url.searchParams.set('q', trimmed);
        } else {
          url.searchParams.delete('q');
          url.searchParams.delete('search');
        }
        window.history.replaceState({}, '', url.toString());
      } catch (e) {
        // Fallback for older browsers
      }
    }

    // Helper: Read query from URL (?q=... or ?search=...)
    static getUrlQuery() {
      if (typeof window === 'undefined' || !window.location) return '';
      try {
        const urlParams = new URLSearchParams(window.location.search);
        return (urlParams.get('q') || urlParams.get('search') || '').trim();
      } catch (e) {
        return '';
      }
    }
  }

  return AppSearchEngine;
});
