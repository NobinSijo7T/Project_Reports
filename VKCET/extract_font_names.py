import fitz
import re

doc = fitz.open('reference.pdf')

for xref in range(1, doc.xref_length()):
    obj = doc.xref_object(xref)
    if '/FontFile2' in obj:
        # get font descriptor
        lines = [l.strip() for l in obj.split('\n') if '/Font' in l or '/Base' in l or '/Type' in l]
        # find the font file xref
        m = re.search(r'/FontFile2\s+(\d+)\s+0\s+R', obj)
        if m:
            ff_xref = int(m.group(1))
            stream = doc.xref_stream(ff_xref)
            # search for Name table strings in TTF
            names = re.findall(rb'[\x20-\x7e]{4,}', stream[:2000])
            print(f"Xref {xref} (FontFile2 {ff_xref}): {lines}")
            for n in names[:5]:
                print(f"    {n.decode('latin1', errors='ignore')}")

