import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    for b in p['blocks']:
        if b['type'] == 'text':
            for l in b['lines']:
                for s in l['spans']:
                    if 'F4' in s['font'] or 'F5' in s['font']:
                        # On pages 1-32, xref 84/98 is F4/F5 = Arial
                        # Wait, let's see which pages
                        txt = s['text'].strip()
                        if txt:
                            print(f"P{pno} {s['font']} sz={round(s['size'],1)}: {repr(txt[:40])}")

