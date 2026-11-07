import fitz

doc = fitz.open('reference.pdf')

for pno in [1, 3]:
    page = doc[pno-1]
    for img in page.get_images():
        xref = img[0]
        rects = page.get_image_rects(xref)
        print(f"Page {pno} Image xref {xref}: rects={rects}")

