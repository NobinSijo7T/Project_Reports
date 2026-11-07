import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    # let's find if there are tables or headings
    txt = p['text'].strip()
    first_few = [l.strip() for l in txt.split('\n') if l.strip()][:3]
    last_few = [l.strip() for l in txt.split('\n') if l.strip()][-2:]
    print(f"=== Page {pno:02d} (len={len(txt)}) ===")
    print(f"   Start: {' // '.join(first_few)}")
    print(f"   End:   {' // '.join(last_few)}")

