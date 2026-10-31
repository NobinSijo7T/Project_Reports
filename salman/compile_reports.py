import subprocess
import shutil
import os

students = [
    {
        "name": "MOHAMMAD SALMAN",
        "roll": "KNP23CS076",
        "tex_file": "main_salaman.tex",
        "base_pdf": "main_salaman.pdf",
        "aliases": ["Salaman.pdf", "Report_MUHAMMED_SALAMAN_KNP23CS076.pdf"]
    },
    {
        "name": "JITHIN JOSEPH",
        "roll": "KNP23CS062",
        "tex_file": "main_jithin.tex",
        "base_pdf": "main_jithin.pdf",
        "aliases": ["Jithin.pdf", "Report_JITHIN_JOSEPH_KNP23CS062.pdf"]
    },
    {
        "name": "PUNYA A J",
        "roll": "KNP23CS087",
        "tex_file": "main_punya.tex",
        "base_pdf": "main_punya.pdf",
        "aliases": ["Punya.pdf", "Report_PUNYA_A_J_KNP23CS087.pdf"]
    },
    {
        "name": "SANA AZEEZ",
        "roll": "KNP23CS092",
        "tex_file": "main_sana.tex",
        "base_pdf": "main_sana.pdf",
        "aliases": ["Sana.pdf", "Report_SANA_AZEEZ_KNP23CS092.pdf"]
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
res_main1 = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], capture_output=True, text=True)
if res_main1.returncode != 0:
    print("Error during main.tex pass 1:")
    print(res_main1.stderr[-1000:] if res_main1.stderr else res_main1.stdout[-1000:])
    exit(1)

res_main2 = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], capture_output=True, text=True)
if res_main2.returncode != 0:
    print("Error during main.tex pass 2:")
    print(res_main2.stderr[-1000:] if res_main2.stderr else res_main2.stdout[-1000:])
    exit(1)

print(f"main.pdf updated successfully ({os.path.getsize('main.pdf')} bytes)")

print("\n=== Verification with pdftotext ===")
for student in students:
    for alias in [student["aliases"][0]]:
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
