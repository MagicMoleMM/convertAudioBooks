import pdfplumber

with pdfplumber.open("uliana.pdf") as pdf:
    first_page = pdf.pages[3]
    print(first_page.extract_text(x_tolerance=1, y_tolerance=1,layout=True, x_density=3, y_density=10))
    
