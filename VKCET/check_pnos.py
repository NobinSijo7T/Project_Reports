import json
with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)
for pno in range(1, 35):
    p = pages[pno-1]
    # search for isolated numbers or roman numerals
    candidates = []
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                ltxt = ''.join(s['text'] for s in l['spans']).strip()
                if l['bbox'][1] > 720:
                    candidates.append((round(l['bbox'][1],1), round(l['bbox'][0],1), ltxt))
    print(f"Page {pno:02d}: bottom lines: {candidates}")

