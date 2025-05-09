# Tugas Pemrograman A
# Kelompok 6: Javana, Ulil, Rivi

import pandas as pandas
import numpy as numpy

def process_data(csv_path):
    # Membaca file CSV dan menghapus data yang hilang (NaN)
    df = pandas.read_csv(csv_path)
    data_bersih = df.dropna()

    # Gunakan data tahun dikurangi 1960 untuk stabilitas numerik
    x = data_bersih['Year'].values - 1960
    netY = data_bersih['Percentage_Internet_User'].values
    popY = data_bersih['Population'].values

    # Hitung koefisien polinomial derajat 3
    koefisienInternet = numpy.polyfit(x, netY, 3)
    koefisienPopulation = numpy.polyfit(x, popY, 3)

    return koefisienInternet, koefisienPopulation

# Format persamaan polinomial ke bentuk string
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

# Membuat fungsi polinomial dari file CSV
def create_polynomial_functions(csv_path):
    df = pandas.read_csv(csv_path)
    data_bersih = df.dropna()

    x = data_bersih['Year'].values
    netY = data_bersih['Percentage_Internet_User'].values
    popY = data_bersih['Population'].values

    # Buat polinomial dari tahun langsung (tanpa -1960)
    koefisienInternet = numpy.polyfit(x, netY, 3)
    koefisienPopulation = numpy.polyfit(x, popY, 3)

    internet_poly = numpy.poly1d(koefisienInternet)
    population_poly = numpy.poly1d(koefisienPopulation)

    return internet_poly, population_poly, koefisienInternet, koefisienPopulation

# Estimasi populasi 2030 dan persentase pengguna internet 2035
def estimasi_tahun_mendatang(pop_func, net_func, tahun_pop=2030, tahun_net=2035):
    estimasi_pop = int(pop_func(tahun_pop))
    estimasi_net = round(net_func(tahun_net), 2)

    # Batasi ke 100% maksimum
    if estimasi_net > 100:
        estimasi_net = 100.0

    return estimasi_pop, estimasi_net

# === MAIN PROGRAM ===

csv_path = "./DataTugasPemrogramanA.csv"

# Proses dan dapatkan fungsi polinomial
internet_poly, population_poly, koefInet, koefPop = create_polynomial_functions(csv_path)

# Format persamaan ke bentuk string
hasilInternet = formatPoly(koefInet, var='x')
hasilPopulation = formatPoly(koefPop, var='x')

# Cetak persamaan
print("Polinomial Internet:")
print(hasilInternet)
print("\nPolinomial Population:")
print(hasilPopulation)

# Estimasi nilai masa depan
predicted_pop_2030, predicted_net_2035 = estimasi_tahun_mendatang(population_poly, internet_poly)

# Cetak hasil estimasi
print("\nEstimasi Tahun Mendatang:")
print(f"- Populasi Indonesia tahun 2030: {predicted_pop_2030} jiwa")
print(f"- Persentase Pengguna Internet tahun 2035: {predicted_net_2035}%")
