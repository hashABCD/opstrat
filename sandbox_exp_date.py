import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'c':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'p':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return option_price

# Define a range of stock prices
stock_prices = np.arange(80, 120, 1)  # Adjust this range as needed

# Example list of options contracts
options_contracts = [
    {'K': 105, 'T': 0.25, 'r': 0.05, 'sigma': 0.2, 'type': 'c'},
    {'K': 95, 'T': 0.25, 'r': 0.05, 'sigma': 0.2, 'type': 'p'},
]

# Create an empty 2D list to store option prices
option_prices = []

# Calculate theoretical prices for each contract at each stock price and store them
for stock_price in stock_prices:
    row = [stock_price]
    for contract in options_contracts:
        theoretical_price = black_scholes(stock_price, contract['K'], contract['T'], contract['r'], contract['sigma'], contract['type'])
        row.append(theoretical_price)
    option_prices.append(row)

# Convert the option_prices list into a NumPy array
option_prices_array = np.array(option_prices)

# Print the resulting array
print(option_prices_array)

x = option_prices_array[:,0]
print(x)
op_list = option_prices_array[:,1]
print(op_list)
y=0

# plt.figure(figsize=(10,6))
# for i in range (len(op_list)):
#     try:
#         contract=str(op_list[i]['contract'])  
#     except:
#         contract='1'
        
#     label=contract+' '+str(abb[op_list[i]['tr_type']])+' '+str(abb[op_list[i]['op_type']])+' ST: '+str(op_list[i]['strike'])
#     sns.lineplot(x=x, y=y_list[i], label=label, alpha=0.5)
#     y+=np.array(y_list[i])

# sns.lineplot(x=x, y=y, label='combined', alpha=1, color='k')
# plt.axhline(color='k', linestyle='--')
# plt.axvline(x=spot, color='r', linestyle='--', label='spot price')
# plt.legend()
# plt.legend(loc='upper right')
# title="Multiple Options Plotter"
# plt.title(title)
# plt.fill_between(x, y, 0, alpha=0.2, where=y>y0, facecolor='green', interpolate=True)
# plt.fill_between(x, y, 0, alpha=0.2, where=y<y0, facecolor='red', interpolate=True)
# plt.tight_layout()
# if save==True:
#     plt.savefig(file)
# plt.show()
