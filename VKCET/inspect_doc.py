import fitz

doc = fitz.open('reference.pdf')

for pno in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 23, 31, 32, 33]:
    page = doc[pno]
    print(f"==================== PAGE {pno+1} ====================")
    blocks = page.get_text('dict')['blocks']
    for b in sorted(blocks, key=lambda b: (b['bbox'][1], b['bbox'][0])):
        if b.get('type') == 0:
            txt = " ".join("".join(s['text'] for s in l['spans']) for l in b['lines']).strip()
            if txt:
                first_span = b['lines'][0]['spans'][0]
                font = first_span['font']
                size = round(first_span['size'], 1)
                bbox = [round(x, 1) for x in b['bbox']]
                print(f"bbox={bbox} font={font} size={size}: {txt[:100]}")

