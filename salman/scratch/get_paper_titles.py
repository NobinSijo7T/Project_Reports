import glob, json, os, re

files = sorted(glob.glob('References/extracted/*.json'))

paper_data = []

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        d = json.load(f)
    text = d.get('full_text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    # We will store raw lines 0-60 and look for metadata
    paper_data.append({
        'filename': fname,
        'pages': d.get('num_pages', 0),
        'top_lines': lines[:60],
        'full_text_start': text[:3000]
    })

# Write to a python inspectable file
with open('scratch/papers_raw_top.json', 'w', encoding='utf-8') as f:
    json.dump(paper_data, f, indent=2)

print(f"Processed {len(paper_data)} papers.")
