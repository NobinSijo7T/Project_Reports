import json

with open('scratch/papers_raw_top.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Let's inspect each paper's filename and first 30 lines
out_lines = []
for i, p in enumerate(papers, 1):
    out_lines.append(f"[{i}] {p['filename']} ({p['pages']} pages)")
    for idx, l in enumerate(p['top_lines'][:20]):
        out_lines.append(f"    {idx}: {l}")
    out_lines.append("")

with open('scratch/papers_index.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out_lines))

print("Wrote scratch/papers_index.txt")
