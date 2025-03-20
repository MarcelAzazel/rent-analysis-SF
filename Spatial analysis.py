import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Arquivos\\Documentos\\Courses\\CCP\\rent.csv\\rent.csv")

sf = data[data['city'] == 'san francisco']

sf_selected = sf[['year', 'nhood', 'price']]

average_rent = sf_selected['price'].mean()

ai = pd.read_csv("C:\\Arquivos\\Documentos\\Courses\\CCP\\AI_Companies.csv")

#print(ai.head())

# print("Average rent price = ", average_rent)

full_nhood = list(sf_selected['nhood'])

nhoods = []

for i in full_nhood:
    if i not in nhoods:
        nhoods.append(i)
    else:
        continue

#print(sorted(nhoods))

full_years = list(sf['year'])

years = []

for i in full_years:
    if i not in years:
        years.append(i)
    else:
        continue

years.sort()

for hood in nhoods:
    for year in years:
        hood_df = sf[sf['nhood'] == hood]
        hood_year_df = hood_df[hood_df['year'] == year]
        average = hood_year_df['price'].mean(skipna=True)
        #print("Average rent in ", hood, " during ", year, " = ", average)

# Function to plot rent price of neighborhood over years
def plot_hood(df, hood):
    prices = []
    hood_sf = df[df['nhood'] == hood]
    for year in years:
        price_year = hood_sf[hood_sf['year'] == year]
        year_mean = price_year['price'].mean()
        prices.append(year_mean)

    years_arr = np.array(years)
    prices_arr = np.array(prices)

    mask = ~np.isnan(prices)

    filtered_years = years_arr[mask]
    filtered_prices = prices_arr[mask]

    plt.plot(filtered_years, filtered_prices)
    plt.xticks(range(min(filtered_years), max(filtered_years) + 1, 1), fontsize=7)
    plt.grid(True)
    plt.title("Rent price over time for " + hood)
    plt.xlabel("Year")
    plt.ylabel("Price\n$ / month")
    plt.show()

def year_rent(df, hood, year):
    hood_df = df[df['nhood'] == hood]
    #print(hood_df.head())
    year_hood_df = hood_df[hood_df['year'] == year]
    #print(hood_df['year'])
    #print(year_hood_df.head())
    average = year_hood_df['price'].mean()
    #print(list(year_hood_df['price']))
    print("Rent price in ", hood, " during ", year, " = ", average)
    return average

plot_hood(sf, 'potrero hill')
#year_rent(sf, 'tenderloin', 2017)

