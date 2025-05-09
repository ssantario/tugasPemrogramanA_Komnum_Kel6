# Tugas Pemrograman A
# Kelompok 6: Javana, Ulil, Rivi

import pandas as pandas 
import numpy as numpy  

csv_path = "../DataTugasPemrogramanA.csv"

df = pandas.read_csv(csv_path)
dataBersih = df.dropna()

# menagambil data dari .csv
x = dataBersih['Year'].values - 1960
netY = dataBersih['Percentage_Internet_User'].values
popY = dataBersih['Population'].values

koefisienInternet = numpy.polyfit(x, netY, 3)
koefisienPopulation = numpy.polyfit(x, popY, 3)

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

hasilInternet = formatPoly(koefisienInternet)
hasilPopulation = formatPoly(koefisienPopulation)

hasilInternet, hasilPopulation