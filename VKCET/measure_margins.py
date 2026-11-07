import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    lefts = []
    rights = []
    tops = []
    bottoms = []
    
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                ltxt = "".join(s['text'] for s in l['spans']).strip()
                if not ltxt: continue
                # ignore page numbers at bottom
                if l['bbox'][1] > 740: continue
                lefts.append(l['bbox'][0])
                rights.append(l['bbox'][2])
                tops.append(l['bbox'][1])
                bottoms.append(l['bbox'][3])
                
    if lefts:
        # 10th percentile and 90th percentile to get body margins
        lefts.sort()
        rights.sort()
        tops.sort()
        bottoms.sort()
        print(f"Page {pno:02d}: left_min={lefts[0]:.1f}, left_p10={lefts[int(len(lefts)*0.1)]:.1f}, right_max={rights[-1]:.1f}, right_p90={rights[int(len(rights)*0.9)]:.1f}, top_min={tops[0]:.1f}, bottom_max={bottoms[-1]:.1f}")

