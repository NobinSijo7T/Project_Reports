import subprocess
import shutil
import os

students = [
    {
        "name": "ALEENA ANILKUMAR",
        "roll": "KNP23CS025",
        "tex_file": "main_aleena.tex",
        "base_pdf": "main_aleena.pdf",
        "aliases": ["Aleena.pdf", "Report_ALEENA_ANILKUMAR_KNP23CS025.pdf"]
    },
    {
        "name": "ABHINAYA P S",
        "roll": "KNP23CO007",
        "tex_file": "main_abhinaya.tex",
        "base_pdf": "main_abhinaya.pdf",
        "aliases": ["Abhinaya.pdf", "Report_ABHINAYA_P_S_KNP23CO007.pdf"]
    },
    {
        "name": "ADITHYA DINESH",
        "roll": "KNP23CS016",
        "tex_file": "main_adithya.tex",
        "base_pdf": "main_adithya.pdf",
        "aliases": ["Adithya.pdf", "Report_ADITHYA_DINESH_KNP23CS016.pdf"]
    },
    {
        "name": "FATHIMA A",
        "roll": "KNP23CS047",
        "tex_file": "main_fathima.tex",
        "base_pdf": "main_fathima.pdf",
        "aliases": ["Fathima.pdf", "Report_FATHIMA_A_KNP23CS047.pdf"]
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
