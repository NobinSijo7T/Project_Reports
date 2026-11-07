import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

p3 = pages[2]
for b in p3['blocks']:
    if b['type'] == 'text':
        for l in b['lines']:
            txt = "".join(s['text'] for s in l['spans']).strip()
            if txt:
                print(f"y={l['bbox'][1]:.1f}: {repr(txt)}")
    elif b['type'] == 'image':
        print(f"IMAGE: y={b['bbox'][1]:.1f} to {b['bbox'][3]:.1f}, w={b['bbox'][2]-b['bbox'][0]:.1f}, h={b['bbox'][3]-b['bbox'][1]:.1f}")

