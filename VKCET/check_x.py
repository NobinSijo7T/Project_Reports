import json
with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)
for pno in [10, 11, 14, 15, 17, 18, 19]:
    p = pages[pno-1]
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                if l['bbox'][0] < 98:
                    ltxt = ''.join(s['text'] for s in l['spans']).strip()
                    if ltxt:
                        print(f"P{pno} x={l['bbox'][0]:.1f}, y={l['bbox'][1]:.1f}: {repr(ltxt[:60])}")

