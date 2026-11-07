import fitz

doc = fitz.open('main.pdf')
print(f"Total pages in main.pdf: {len(doc)}")

for i in range(len(doc)):
    txt = doc[i].get_text().strip()
    first_line = txt.split('\n')[0] if txt else 'EMPTY'
    last_line = txt.split('\n')[-1] if txt else 'EMPTY'
    print(f"Page {i+1:02d}: lines={len(txt.splitlines())} | First: {repr(first_line[:40])} | Last: {repr(last_line[:40])}")

