import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for pno in [4, 5]:
    p = pages[pno-1]
    print(f"=== PAGE {pno} ===")
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                txt = "".join(s['text'] for s in l['spans']).strip()
                if txt:
                    print(f"y={l['bbox'][1]:.1f}: {repr(txt[:60])}")

