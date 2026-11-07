import os

for pno in range(10, 35):
    fname = f"page_texts/page_{pno:02d}.txt"
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.splitlines()
    print(f"=== PAGE {pno} (report page {pno-9}) ===")
    print(f"Total lines: {len(lines)}")
    # print all lines if less than 15, or head and tail
    for l in lines:
        if any(l.startswith(h) for h in ["CHAPTER", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "CONCLUSION", "REFERENCES", "Table ", "Step "]):
            print(f"   [HEADING/TABLE]: {l}")

