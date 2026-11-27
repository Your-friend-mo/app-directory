import os
import re
import json

BASE_DIR = r"c:\Users\m\Documents\app-catalog"

PAGE_KEYWORDS = {
    "index.html": "AppDirectory",
    "about.html": "AppDirectory",
    "contact.html": "AppDirectory",
    "privacy.html": "AppDirectory",
    "terms.html": "AppDirectory",
    "vscodium.html": "VSCodium",
    "obsidian.html": "Obsidian",
    "bitwarden.html": "Bitwarden",
    "vlc.html": "VLC",
    "signal.html": "Signal",
    "7zip.html": "7-Zip",
    "kdenlive.html": "Kdenlive",
    "syncthing.html": "Syncthing",
    "hoppscotch.html": "Hoppscotch",
    "supertuxkart.html": "SuperTuxKart",
    "0ad.html": "0 A.D.",
    "mindustry.html": "Mindustry",
    "openttd.html": "OpenTTD",
    "wesnoth.html": "Wesnoth",
    "veloren.html": "Veloren",
    "cataclysm-dda.html": "Cataclysm: DDA",
    "xonotic.html": "Xonotic",
    "flightgear.html": "FlightGear"
}

def audit_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    issues = []

    # 1. H1 Check
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
    if len(h1s) == 0:
        issues.append("Missing H1 tag")
    elif len(h1s) > 1:
        issues.append(f"Multiple H1 tags ({len(h1s)})")

    # 2. H2 Check
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL | re.IGNORECASE)
    if len(h2s) < 1:
        issues.append("Missing H2 tag")

    # 3. H3 Check
    h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', content, re.DOTALL | re.IGNORECASE)
    if len(h3s) < 1:
        issues.append("Missing H3 tag")

    # 4. Meta Description Check (100-165 chars)
    m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    desc_len = 0
    if not m_desc:
        issues.append("Missing meta description")
    else:
        desc_len = len(m_desc.group(1))
        if desc_len < 100 or desc_len > 165:
            issues.append(f"Meta description length outside target range: {desc_len} chars")

    # 5. Meta Title Check
    m_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title_len = 0
    if not m_title:
        issues.append("Missing title")
    else:
        title_len = len(m_title.group(1))

    # 6. Canonical URL Check
    m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    if not m_canon:
        issues.append("Missing canonical URL")

    # 7. Open Graph Tags Check
    og_title = re.search(r'<meta\s+property=["\']og:title["\']', content, re.IGNORECASE)
    og_desc = re.search(r'<meta\s+property=["\']og:description["\']', content, re.IGNORECASE)
    if not og_title or not og_desc:
        issues.append("Missing OpenGraph tags")

    # 8. Schema.org JSON-LD Check
    schema_match = re.search(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    if not schema_match:
        issues.append("Missing JSON-LD schema")
    else:
        try:
            json.loads(schema_match.group(1))
        except Exception as e:
            issues.append(f"Invalid JSON-LD schema: {e}")

    # 9. Keyword Density Check (Target: ~2.0%, allowed 1.80% - 2.20%)
    kw = PAGE_KEYWORDS.get(filename, "AppDirectory")
    clean_text = re.sub(r'<script.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    clean_text = re.sub(r'<style.*?</style>', ' ', clean_text, flags=re.DOTALL | re.IGNORECASE)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    clean_text = re.sub(r'&[a-zA-Z0-9#]+;', ' ', clean_text)
    words = re.findall(r'[a-zA-Z0-9\._\-]+', clean_text)
    total_w = len(words)
    kw_count = len(re.findall(re.escape(kw), clean_text, flags=re.IGNORECASE))
    density = (kw_count / total_w * 100) if total_w > 0 else 0

    if density < 1.80 or density > 2.20:
        issues.append(f"Keyword density for '{kw}' outside target 2%: {density:.2f}% ({kw_count}/{total_w})")

    return {
        "file": filename,
        "keyword": kw,
        "kw_count": kw_count,
        "total_words": total_w,
        "density": density,
        "h1_count": len(h1s),
        "h2_count": len(h2s),
        "h3_count": len(h3s),
        "desc_len": desc_len,
        "title_len": title_len,
        "issues": issues
    }

# Scan all html files
html_files = [
    os.path.join(BASE_DIR, "index.html"),
    os.path.join(BASE_DIR, "about.html"),
    os.path.join(BASE_DIR, "contact.html"),
    os.path.join(BASE_DIR, "privacy.html"),
    os.path.join(BASE_DIR, "terms.html"),
]
apps_dir = os.path.join(BASE_DIR, "apps")
if os.path.exists(apps_dir):
    for f in sorted(os.listdir(apps_dir)):
        if f.endswith(".html"):
            html_files.append(os.path.join(apps_dir, f))

print(f"Auditing {len(html_files)} HTML pages with SEO standards & 2% keyword density check...")
all_passed = True
for path in html_files:
    res = audit_html(path)
    if res["issues"]:
        all_passed = False
        print(f"[FAIL] {res['file']}: {res['issues']}")
    else:
        print(f"[PASS] {res['file']} (H1: {res['h1_count']}, H2: {res['h2_count']}, H3: {res['h3_count']}, Title: {res['title_len']}c, Desc: {res['desc_len']}c, '{res['keyword']}': {res['kw_count']}/{res['total_words']} = {res['density']:.2f}%)")

if all_passed:
    print("\nSUCCESS: All 23 pages meet ALL SEO criteria and 2% keyword density requirement!")
else:
    print("\nFAIL: Some pages failed validation.")
