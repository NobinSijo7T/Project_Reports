import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for pno in [10, 11, 13, 14, 15, 17, 18, 19, 21, 24, 27, 30, 32]:
    p = pages[pno-1]
    deltas = []
    lines = []
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                if l['bbox'][1] > 745: continue
                txt = "".join(s['text'] for s in l['spans']).strip()
                if txt:
                    lines.append(l['bbox'][1])
    for j in range(1, len(lines)):
        d = lines[j] - lines[j-1]
        if 15 < d < 35: # line delta within paragraph
            deltas.append(d)
    avg_d = sum(deltas) / len(deltas) if deltas else 0
    min_d = min(deltas) if deltas else 0
    max_d = max(deltas) if deltas else 0
    print(f"P{pno:02d}: count={len(lines)}, within-para line delta: avg={avg_d:.2f}, min={min_d:.2f}, max={max_d:.2f}")

