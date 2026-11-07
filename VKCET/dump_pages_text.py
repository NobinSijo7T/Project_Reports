import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    print(f"\n############################# PAGE {pno} #############################")
    for b in p['blocks']:
        if b['type'] == 'text':
            block_str = ""
            for l in b['lines']:
                line_str = "".join(s['text'] for s in l['spans']).strip()
                if line_str:
                    block_str += line_str + "\n"
            if block_str.strip():
                print(f"[{b['bbox'][0]:.1f}, {b['bbox'][1]:.1f}, {b['bbox'][2]:.1f}, {b['bbox'][3]:.1f}]:")
                print(block_str.rstrip())
        elif b['type'] == 'image':
            print(f"[IMAGE bbox={b['bbox']} size={b['width']}x{b['height']}]")

