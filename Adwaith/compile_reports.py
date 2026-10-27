import subprocess
import shutil
import os

students = [
    {
        "name": "ADWAITH K RAJEESH",
        "roll": "KNP23CS018",
        "tex_file": "main_adwaith.tex",
        "base_pdf": "main_adwaith.pdf",
        "aliases": ["Adwaith.pdf", "Report_ADWAITH_K_RAJEESH_KNP23CS018.pdf"]
    },
    {
        "name": "ANAMIKA P",
        "roll": "KNP23CS029",
        "tex_file": "main_anamika.tex",
        "base_pdf": "main_anamika.pdf",
        "aliases": ["Anamika.pdf", "Report_ANAMIKA_P_KNP23CS029.pdf"]
    },
    {
        "name": "GEORGY BINU GEORGE",
        "roll": "KNP23CS048",
        "tex_file": "main_georgy.tex",
        "base_pdf": "main_georgy.pdf",
        "aliases": ["Georgy.pdf", "Report_GEORGY_BINU_GEORGE_KNP23CS048.pdf"]
    },
    {
        "name": "INSHAD IBRAHIM C",
        "roll": "KNP23CS055",
        "tex_file": "main_inshad.tex",
        "base_pdf": "main_inshad.pdf",
        "aliases": ["Inshad.pdf", "Report_INSHAD_IBRAHIM_C_KNP23CS055.pdf"]
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

print("\n=== Verification with pdftotext ===")
for student in students:
    for alias in [student["aliases"][0]]:
        cmd = ["pdftotext", "-f", "4", "-l", "4", alias, "-"]
        txt_proc = subprocess.run(cmd, capture_output=True, text=True)
        out = txt_proc.stdout
        normalized_out = " ".join(out.split())
        has_name = student["name"] in normalized_out
        has_roll = student["roll"] in normalized_out
        print(f"{alias} Page 4 Certificate Check: Name match={has_name}, Roll match={has_roll}")
        if not (has_name and has_roll):
            print(f"ERROR: Verification failed for {alias}!")
            print(out)
            exit(1)

print("\nAll reports compiled and verified successfully!")
