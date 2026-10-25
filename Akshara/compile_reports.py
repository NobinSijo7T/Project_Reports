import subprocess
import shutil
import os

students = [
    {
        "name": "DEVIKA P A",
        "roll": "KNP23CS042",
        "tex_file": "main_devika.tex",
        "base_pdf": "main_devika.pdf",
        "aliases": ["Devika.pdf", "Report_DEVIKA_P_A_KNP23CS042.pdf"]
    },
    {
        "name": "ASWATHY S",
        "roll": "KNP23CS038",
        "tex_file": "main_aswathy.tex",
        "base_pdf": "main_aswathy.pdf",
        "aliases": ["Aswathy.pdf", "Report_ASWATHY_S_KNP23CS038.pdf"]
    },
    {
        "name": "AKSHARA N LEO MATHEW",
        "roll": "KNP23CS023",
        "tex_file": "main_akshara.tex",
        "base_pdf": "main_akshara.pdf",
        "aliases": ["Akshara.pdf", "Report_AKSHARA_N_LEO_MATHEW_KNP23CS023.pdf"]
    }
]

print("=== Compiling all 3 individual B.Tech Project Reports ===")

for student in students:
    tex = student["tex_file"]
    print(f"\n--- Processing {student['name']} ({student['roll']}) using {tex} ---")
    
    # Pass 1
    res1 = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex], capture_output=True, text=True)
    if res1.returncode != 0:
        print(f"Error during pass 1 for {tex}:")
        print(res1.stderr[-1000:] if res1.stderr else res1.stdout[-1000:])
        exit(1)
        
    # Pass 2 (resolves TOC, LOF, LOT, cross-references)
    res2 = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex], capture_output=True, text=True)
    if res2.returncode != 0:
        print(f"Error during pass 2 for {tex}:")
        print(res2.stderr[-1000:] if res2.stderr else res2.stdout[-1000:])
        exit(1)

    base_pdf = student["base_pdf"]
    if os.path.exists(base_pdf):
        size = os.path.getsize(base_pdf)
        print(f"Successfully generated {base_pdf} ({size} bytes)")
        
        # Copy to user-friendly aliases
        for alias in student["aliases"]:
            shutil.copyfile(base_pdf, alias)
            print(f"  -> Created alias: {alias}")
    else:
        print(f"ERROR: Expected PDF {base_pdf} was not found!")
        exit(1)

# Also compile main.tex twice to keep main.pdf completely up to date
print("\n--- Compiling main.tex ---")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], capture_output=True)
subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], capture_output=True)
print(f"main.pdf updated successfully ({os.path.getsize('main.pdf')} bytes)")

print("\n=== Verification with pdftotext ===")
for student in students:
    for alias in [student["aliases"][0]]:
        # Page 4 is the individual certificate page (page 1: cover, page 2: vision/mission, page 3: group cert, page 4: individual cert)
        cmd = ["pdftotext", "-f", "4", "-l", "4", alias, "-"]
        txt_proc = subprocess.run(cmd, capture_output=True, text=True)
        out = txt_proc.stdout
        has_name = student["name"] in out
        has_roll = student["roll"] in out
        print(f"{alias} Page 4 Certificate Check: Name match={has_name}, Roll match={has_roll}")
        if not (has_name and has_roll):
            print(f"ERROR: Verification failed for {alias}!")
            print(out)
            exit(1)

print("\nAll reports compiled and verified successfully!")
