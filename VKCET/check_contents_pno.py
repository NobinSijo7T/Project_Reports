import json
with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for pno in [5, 6, 7]:
    p = pages[pno-1]
    print(f"=== PAGE {pno} all spans ===")
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                for s in l['spans']:
                    if s['bbox'][1] > 650:
                        print(f"y={s['bbox'][1]:.1f}, x={s['bbox'][0]:.1f}, text={repr(s['text'])}")

