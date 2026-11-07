import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Inspect page 10 lines
p10 = pages[9]
for b in p10['blocks']:
    if b['type'] == 'text':
        for i, l in enumerate(b['lines']):
            txt = "".join(s['text'] for s in l['spans']).strip()
            if txt:
                print(f"y0={l['bbox'][1]:.2f}, y1={l['bbox'][3]:.2f}, h={l['bbox'][3]-l['bbox'][1]:.2f}: {repr(txt[:40])}")

