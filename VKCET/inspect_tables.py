import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for pno in [16, 24, 25, 26]:
    p = pages[pno-1]
    print(f"======================================== PAGE {pno} ========================================")
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                ltxt = "".join(s['text'] for s in l['spans']).strip()
                if ltxt:
                    print(f"[{l['bbox'][0]:5.1f}, {l['bbox'][1]:5.1f}, {l['bbox'][2]:5.1f}, {l['bbox'][3]:5.1f}]: {ltxt}")

