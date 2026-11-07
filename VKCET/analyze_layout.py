import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    # find lines at the very top (y < 80) and very bottom (y > 720)
    top_lines = []
    bottom_lines = []
    body_lines = []
    fonts_used = set()
    sizes_used = set()
    
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                ltxt = "".join(s['text'] for s in l['spans']).strip()
                if not ltxt: continue
                y = l['bbox'][1]
                for s in l['spans']:
                    fonts_used.add(s['font'])
                    sizes_used.add(round(s['size'], 1))
                if y < 70:
                    top_lines.append((round(y,1), ltxt))
                elif y > 730:
                    bottom_lines.append((round(y,1), ltxt))
                else:
                    body_lines.append((round(y,1), ltxt))
                    
    print(f"=== PAGE {pno} (fonts: {list(fonts_used)[:3]}, sizes: {sorted(list(sizes_used))}) ===")
    if top_lines:
        print(f"  TOP: {top_lines}")
    if bottom_lines:
        print(f"  BOTTOM: {bottom_lines}")
    # print first 2 body lines and last body line
    if body_lines:
        print(f"  BODY first: {body_lines[0]}")
        if len(body_lines) > 1:
            print(f"  BODY second: {body_lines[1]}")
        print(f"  BODY last: {body_lines[-1]}")

