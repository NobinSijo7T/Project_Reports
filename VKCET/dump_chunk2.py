def check_page_content(start_p, end_p):
    for p in range(start_p, end_p + 1):
        with open(f"page_texts/page_{p:02d}.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        print(f"\n==================== PAGE {p} ====================")
        for l in lines:
            print(l)

check_page_content(16, 23)

