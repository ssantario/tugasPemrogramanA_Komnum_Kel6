import pandas as pd
import numpy as np

def predict_future_population_and_internet(csv_path):
    # Membaca data dari file CSV
    data = pd.read_csv(csv_path)
    # Mengambil kolom tahun, populasi, dan persentase pengguna internet
    years = data["Year"]
    population = data["Population"]
    internet = data["Percentage_Internet_User"]


    # Menggunakan regresi polinomial derajat 3 untuk memodelkan data populasi dan internet
    # np.polyfit adalah fungsi dari NumPy yang digunakan untuk melakukan regresi polinomial
    # years adalah x values, population dan internet adalah y values
    # 3 adalah derajat polinomial yang digunakan
    # Dalam hal ini, kita menggunakan derajat 3 untuk mendapatkan kurva yang lebih halus
    pop_coeffs = np.polyfit(years, population, 3)  
    net_coeffs = np.polyfit(years, internet, 3)    


    # Membuat fungsi polinomial berdasarkan koefisien yang diperoleh
    # Mengubah array koefisien menjadi fungsi polinomial yang bisa dievaluasi seperti fungsi matematika.
    pop_poly = np.poly1d(pop_coeffs)  
    net_poly = np.poly1d(net_coeffs)  


    # Memprediksi populasi menggunakan fungsi polinomial yang telah dibuat
    # pada tahun 2030 dan persentase pengguna internet pada tahun 2035
    pred_2030_pop = int(pop_poly(2030))  
    pred_2035_net = round(net_poly(2035), 2) 


    return pred_2030_pop, pred_2035_net


# Path file CSV
csv_path = "./DataTugasPemrogramanA.csv" 
pop_2030, net_2035 = predict_future_population_and_internet(csv_path)


print(f"Estimated Population in 2030: {pop_2030}")  
print(f"Estimated Internet Usage in 2035: {net_2035}%") 