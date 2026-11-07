import fitz

doc = fitz.open('reference.pdf')

for pno in [1, 2, 3, 16, 24, 25, 26]:
    page = doc[pno-1]
    drawings = page.get_drawings()
    print(f"Page {pno}: {len(drawings)} drawings")
    for d in drawings[:10]:
        print(f"   type: {d.get('type')}, rect: {d.get('rect')}, color: {d.get('color')}, fill: {d.get('fill')}, width: {d.get('width')}")

