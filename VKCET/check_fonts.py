import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Inspect font usage by page and element
for pno in range(1, 35):
    p = pages[pno-1]
    spans_info = []
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                for s in l['spans']:
                    txt = s['text'].strip()
                    if txt:
                        spans_info.append((s['font'], round(s['size'], 1), s['flags'], txt))
    # print unique combinations of (font, size, flags)
    combos = set((f, sz, fl) for f, sz, fl, t in spans_info)
    print(f"P{pno:02d}: {combos}")

