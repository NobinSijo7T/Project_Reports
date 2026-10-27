import subprocess
import shutil
import os

students = [
    {
        "name": "ADHIL N",
        "roll": "KNP23CS014",
        "tex_file": "main_adhil.tex",
        "base_pdf": "main_adhil.pdf",
        "aliases": ["Adhil.pdf", "Report_ADHIL_N_KNP23CS014.pdf"]
    },
    {
        "name": "ADARSH A S",
        "roll": "KNP23CS010",
        "tex_file": "main_adarsh.tex",
        "base_pdf": "main_adarsh.pdf",
        "aliases": ["Adarsh.pdf", "Report_ADARSH_A_S_KNP23CS010.pdf"]
    },
    {
        "name": "ADWAITH RAJ",
        "roll": "KNP23CS019",
        "tex_file": "main_adwaith.tex",
        "base_pdf": "main_adwaith.pdf",
        "aliases": ["Adwaith.pdf", "Report_ADWAITH_RAJ_KNP23CS019.pdf"]
    },
    {
        "name": "ABHISHEK SURESH",
        "roll": "KNP23CS008",
        "tex_file": "main_abhishek.tex",
        "base_pdf": "main_abhishek.pdf",
        "aliases": ["Abhishek.pdf", "Report_ABHISHEK_SURESH_KNP23CS008.pdf"]
    }
]

print("=== Compiling all 4 individual B.Tech Project Reports ===")

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

print("\nAll reports compiled successfully!")
