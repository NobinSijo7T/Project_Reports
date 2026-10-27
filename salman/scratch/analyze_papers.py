import os
import json
import glob
import re

files = glob.glob('References/extracted/*.json')
print(f"Total json files: {len(files)}")

output_summary = []

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        data = json.load(f)
    text = data.get('full_text', '')
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    header = lines[:30]
    
    # Try finding title, authors, year, abstract
    abstract = ""
    for i, line in enumerate(lines[:100]):
        if re.match(r'^(abstract|ABSTRACT)', line):
            abstract = " ".join(lines[i:i+15])
            break
            
    output_summary.append({
        'file': fname,
        'pages': data.get('num_pages'),
        'top_lines': header[:12],
        'abstract_preview': abstract[:400]
    })

with open('scratch/papers_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(output_summary, f, indent=2)

print("Saved analysis of all papers to scratch/papers_analysis.json")
