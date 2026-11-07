import re

with open("build_full_tex.py", "r", encoding="utf-8") as f:
    code = f.read()

# In Page 6 (Contents), add \setlength{\parskip}{0pt}
old_p6 = r'''% ==================== PAGE 6: CONTENTS (PART 1) ====================
\thispagestyle{empty}
\vspace*{-10pt}
{\centering\fontsize{13.2pt}{15pt}\selectfont\bfseries CONTENTS\par}
\vspace{8pt}

\fontsize{11.3pt}{12.4pt}\selectfont'''

new_p6 = r'''% ==================== PAGE 6: CONTENTS (PART 1) ====================
\thispagestyle{empty}
\vspace*{-10pt}
{\centering\fontsize{13.2pt}{15pt}\selectfont\bfseries CONTENTS\par}
\vspace{6pt}

\begingroup
\setlength{\parskip}{0pt}
\fontsize{11.3pt}{12.2pt}\selectfont'''

old_p7 = r'''% ==================== PAGE 7: CONTENTS (PART 2) ====================
\thispagestyle{empty}
\vspace*{-12pt}
\fontsize{11.3pt}{12.4pt}\selectfont'''

new_p7 = r'''\endgroup
\newpage

% ==================== PAGE 7: CONTENTS (PART 2) ====================
\thispagestyle{empty}
\vspace*{-12pt}
\begingroup
\setlength{\parskip}{0pt}
\fontsize{11.3pt}{12.2pt}\selectfont'''

old_p8 = r'''% ==================== PAGE 8: LIST OF TABLES ====================
\setcounter{page}{5}
\frontmattertitle{LIST OF TABLES}'''

new_p8 = r'''\endgroup
\newpage

% ==================== PAGE 8: LIST OF TABLES ====================
\setcounter{page}{5}
\frontmattertitle{LIST OF TABLES}'''

code = code.replace(old_p6, new_p6)
code = code.replace(old_p7, new_p7)
code = code.replace(old_p8, new_p8)

with open("build_full_tex.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_full_tex.py with parskip=0pt in Contents")

