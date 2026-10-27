import os
import json
import glob
import re

files = sorted(glob.glob('References/extracted/*.json'))
print(f"Found {len(files)} files.")

results = []

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        data = json.load(f)
    text = data.get('full_text', '')
    pages = data.get('num_pages', 0)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    first_page = lines[:50]
    
    # Try finding title and authors
    # Let's save the first 40 lines
    results.append({
        'filename': fname,
        'pages': pages,
        'first_lines': lines[:35],
        'text_snippet': text[:2000]
    })

with open('scratch/papers_detailed.txt', 'w', encoding='utf-8') as out:
    for idx, r in enumerate(results, 1):
        out.write(f"\n{'='*70}\n")
        out.write(f"PAPER {idx}: {r['filename']} ({r['pages']} pages)\n")
        out.write(f"{'='*70}\n")
        out.write("FIRST 25 LINES:\n")
        for l in r['first_lines'][:25]:
            out.write(f"  {l}\n")
        out.write("\nSNIPPET:\n")
        out.write(r['text_snippet'] + "\n")

print("Wrote scratch/papers_detailed.txt successfully.")
