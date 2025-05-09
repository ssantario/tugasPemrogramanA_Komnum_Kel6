import pandas as pd
import numpy as np

def predict_future_population_and_internet(csv_path):
    # Load data
    data = pd.read_csv(csv_path)
    years = data["Year"]
    population = data["Population"]
    internet = data["Percentage_Internet_User"]

    # Fit cubic polynomials
    pop_coeffs = np.polyfit(years, population, 3)
    net_coeffs = np.polyfit(years, internet, 3)

    pop_poly = np.poly1d(pop_coeffs)
    net_poly = np.poly1d(net_coeffs)

    # Predict values
    pred_2030_pop = int(pop_poly(2030))
    pred_2035_net = round(net_poly(2035), 2)

    return pred_2030_pop, pred_2035_net

# Example usage
csv_path = "./DataTugasPemrogramanA.csv" 
pop_2030, net_2035 = predict_future_population_and_internet(csv_path)

print(f"Estimated Population in 2030: {pop_2030}")
print(f"Estimated Internet Usage in 2035: {net_2035}%")