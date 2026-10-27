import json

with open('scratch/papers_analysis.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

for i, p in enumerate(papers, 1):
    print(f"=== Paper {i}: {p['file']} ({p['pages']} pages) ===")
    print("Header lines:")
    for line in p['top_lines'][:6]:
        print("  ", line[:100])
    if p['abstract_preview']:
        print("Abstract preview:", p['abstract_preview'][:200])
    print()
