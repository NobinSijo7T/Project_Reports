$targets = @('main', 'main_Adeeba', 'main_Avani', 'main_Thara')
foreach ($t in $targets) {
    Write-Host "Compiling $t (pass 1)..."
    & pdflatex -interaction=nonstopmode "$t.tex" | Out-Null
    Write-Host "Compiling $t (pass 2)..."
    & pdflatex -interaction=nonstopmode "$t.tex" | Out-Null
}

Write-Host "Compiling scratch/test_cover.tex..."
& pdflatex -interaction=nonstopmode -output-directory=scratch "scratch/test_cover.tex" | Out-Null

Write-Host "Updating reports and reports_duplicates..."
Copy-Item -Force main.pdf reports/main.pdf
Copy-Item -Force main_Adeeba.pdf reports/Report_ADEEBA_ABDUL_VAHID_KNP23CS011.pdf
Copy-Item -Force main_Avani.pdf reports/Report_AVANI_P_LKNP23CS114.pdf
Copy-Item -Force main_Thara.pdf reports/Report_THARA_A_LKNP23CS117.pdf

Copy-Item -Force main_Adeeba.pdf reports_duplicates/Adeeba.pdf
Copy-Item -Force main_Adeeba.pdf reports_duplicates/Adeeba_Abdul_Vahid_KNP23CS011.pdf
Copy-Item -Force main_Adeeba.pdf reports_duplicates/main_Adeeba.pdf

Copy-Item -Force main_Avani.pdf reports_duplicates/Avani.pdf
Copy-Item -Force main_Avani.pdf reports_duplicates/Avani_P_LKNP23CS114.pdf
Copy-Item -Force main_Avani.pdf reports_duplicates/main_Avani.pdf

Copy-Item -Force main_Thara.pdf reports_duplicates/Thara.pdf
Copy-Item -Force main_Thara.pdf reports_duplicates/Thara_A_LKNP23CS117.pdf
Copy-Item -Force main_Thara.pdf reports_duplicates/main_Thara.pdf

Write-Host "All compilations and copies completed successfully!"

