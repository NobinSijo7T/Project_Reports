import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    # Check for special characters
    special_chars = set()
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                for s in l['spans']:
                    for ch in s['text']:
                        if ord(ch) > 127:
                            special_chars.add((ch, hex(ord(ch))))
    if special_chars:
        print(f"P{pno}: {special_chars}")

