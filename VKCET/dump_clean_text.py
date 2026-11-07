import json
import os

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

os.makedirs('page_texts', exist_ok=True)

for p in pages:
    pno = p['page_num']
    lines = []
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                ltxt = "".join(s['text'] for s in l['spans']).strip()
                if ltxt:
                    lines.append(ltxt)
    with open(f"page_texts/page_{pno:02d}.txt", "w", encoding="utf-8") as pf:
        pf.write("\n".join(lines))

print("Dumped all 34 page texts to page_texts/")

