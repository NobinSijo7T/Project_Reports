import fitz

doc = fitz.open('report.pdf')
ref = fitz.open('reference.pdf')
print(f"report.pdf pages: {len(doc)}, reference.pdf pages: {len(ref)}")

for i in range(len(doc)):
    txt = doc[i].get_text().strip()
    first_line = txt.split('\n')[0] if txt else 'EMPTY'
    last_line = txt.split('\n')[-1] if txt else 'EMPTY'
    print(f"Page {i+1:02d}: lines={len(txt.splitlines()):2d} | First: {repr(first_line[:35])} | Last: {repr(last_line[:35])}")

