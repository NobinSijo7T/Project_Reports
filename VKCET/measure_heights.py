import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    y_vals = []
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                if l['bbox'][1] > 745: continue # ignore footer
                txt = "".join(s['text'] for s in l['spans']).strip()
                if txt:
                    y_vals.append(l['bbox'][1])
                    y_vals.append(l['bbox'][3])
    if y_vals:
        min_y = min(y_vals)
        max_y = max(y_vals)
        span_y = max_y - min_y
        print(f"Page {pno:02d}: min_y={min_y:.1f}, max_y={max_y:.1f}, span={span_y:.1f}")

