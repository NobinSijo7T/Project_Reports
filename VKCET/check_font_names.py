import fitz

doc = fitz.open('reference.pdf')

for page in [doc[0], doc[9], doc[32]]:
    print(f"Page {page.number+1} fonts:")
    for f in page.get_fonts():
        xref = f[0]
        # find font name
        obj = doc.xref_object(xref)
        fontname = f[3]
        print(f"  xref {xref}: {f[4]} -> {fontname} (type: {f[2]})")

