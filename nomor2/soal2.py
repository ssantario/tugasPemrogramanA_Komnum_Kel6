# Tugas Pemrograman A
# Kelompok 6: Javana, Ulil, Rivi

import pandas as pandas 
import numpy as numpy  

def process_data(csv_path):
    # read csv kemudian ambil datanya sesuai dengan kolom
    # setelah itu, ya menghitung polinimial memakai numfit
    df = pandas.read_csv(csv_path)
    dataBersih = df.dropna()
    
    x = dataBersih['Year'].values - 1960
    netY = dataBersih['Percentage_Internet_User'].values
    popY = dataBersih['Population'].values
    
    # ini adalah numpy polyfit yang dipakai, saya menggunakan
    # referensi pada https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html 
    koefisienInternet = numpy.polyfit(x, netY, 3)
    koefisienPopulation = numpy.polyfit(x, popY, 3)
    
    return koefisienInternet, koefisienPopulation

# memformat output (dengan bantuan AI GPT)
def formatPoly(coefs, var='x'):
    degree = len(coefs) - 1
    terms = []
    for i, c in enumerate(coefs):
        power = degree - i
        cStr = f"{c:.6f}"
        if power == 0:
            terms.append(f"{cStr}")
        elif power == 1:
            terms.append(f"{cStr}{var}")
        else:
            terms.append(f"{cStr}{var}^{power}")    
    return "y = " + " + ".join(terms)

csv_path = "../DataTugasPemrogramanA.csv"
koefisienInternet, koefisienPopulation = process_data(csv_path)
    
hasilInternet = formatPoly(koefisienInternet)
hasilPopulation = formatPoly(koefisienPopulation)
    
print("polinomial internet:")
print(hasilInternet)
print("\polinomial Population:")
print(hasilPopulation)