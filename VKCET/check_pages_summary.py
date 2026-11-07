for pno in range(10, 35):
    with open(f"page_texts/page_{pno:02d}.txt", "r", encoding="utf-8") as f:
        content = f.read().splitlines()
    print(f"=== Page {pno} (lines: {len(content)}) ===")
    print("  First 3 lines:", content[:3])
    print("  Last 3 lines: ", content[-3:])

