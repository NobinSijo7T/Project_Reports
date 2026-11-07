import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

def show_page_detail(pno):
    p = pages[pno-1]
    print(f"======================================== PAGE {pno} ========================================")
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                line_text = "".join(s['text'] for s in l['spans'])
                font_info = "/".join(f"{s['font']}:{s['size']:.1f}" for s in l['spans'])
                print(f"[{l['bbox'][0]:5.1f}, {l['bbox'][1]:5.1f}, {l['bbox'][2]:5.1f}, {l['bbox'][3]:5.1f}] ({font_info}): {line_text}")
        elif b['type'] == 'image':
            print(f"[IMAGE bbox={b['bbox']}]")

# Let's inspect pages 1, 2, 3, 8, 9
for p in [1, 2, 3]:
    show_page_detail(p)

