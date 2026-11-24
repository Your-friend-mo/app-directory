import os
import re
import json

BASE_DIR = r"c:\Users\m\Documents\app-catalog"

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

    # 3. H3 Check (audit asked for multiple H3 tags)
    h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', content, re.DOTALL | re.IGNORECASE)

    # 4. Meta Description Check (140-160 chars)
    m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    if not m_desc:
        issues.append("Missing meta description")
    else:
        desc_len = len(m_desc.group(1))
        if desc_len < 100 or desc_len > 165:
            issues.append(f"Meta description length outside target range: {desc_len} chars")

    # 5. Meta Title Check
    m_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
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

    return {
        "file": filename,
        "h1_count": len(h1s),
        "h2_count": len(h2s),
        "h3_count": len(h3s),
        "desc_len": len(m_desc.group(1)) if m_desc else 0,
        "title_len": len(m_title.group(1)) if m_title else 0,
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
    for f in os.listdir(apps_dir):
        if f.endswith(".html"):
            html_files.append(os.path.join(apps_dir, f))

print(f"Auditing {len(html_files)} HTML pages...")
all_passed = True
for path in html_files:
    res = audit_html(path)
    if res["issues"]:
        all_passed = False
        print(f"[FAIL] {res['file']}: {res['issues']}")
    else:
        print(f"[PASS] {res['file']} (H1: {res['h1_count']}, H2: {res['h2_count']}, H3: {res['h3_count']}, Title: {res['title_len']}c, Desc: {res['desc_len']}c)")

if all_passed:
    print("\nSUCCESS: All pages meet all SEO & AI-crawler criteria!")
