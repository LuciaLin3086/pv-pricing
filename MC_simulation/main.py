from math import exp

from src.simulator import PriceSimulator
from src.payoff import Payoff

# hyperparameter
n = 20  # 重複 20 次 Monte Carlo
N = 10000 # 抽樣 10000 次得一個option price
S0 = 100
r = 0.05
q = 0.02
sigma = 0.5
T = 0.5
K = 90


# get simulated prices
price_simulator = PriceSimulator(N, n, S0, r, q, sigma, T)
price_matrix = price_simulator.price_simulate()

###############
# Vanilla Calls
###############
# get payoff_matrix by price_matrix
call_payoff = Payoff(K, "C")
call_payoff_matrix = call_payoff.get_payoff_matrix(price_matrix)

# get option values by discounted payoff
call_values = exp(-r * T) * call_payoff_matrix.mean(axis = 1)

CI1 = call_values.mean() - 2 * call_values.std()
CI2 = call_values.mean() + 2 * call_values.std()
print(f"Call value: {call_values.mean()}")
print(f"95% C.I. of call option:[{CI1},{CI2}]")

##############
# Vanilla Puts
##############
# get payoff_matrix by price_matrix
call_payoff = Payoff(K, "P")
call_payoff_matrix = call_payoff.get_payoff_matrix(price_matrix)

# get option values by discounted payoff
call_values = exp(-r * T) * call_payoff_matrix.mean(axis = 1)

CI1 = call_values.mean() - 2 * call_values.std()
CI2 = call_values.mean() + 2 * call_values.std()
print(f"\nPut value: {call_values.mean()}")
print(f"95% C.I. of put option:[{CI1},{CI2}]")

#### for testing
# n = 20
# N = 10000
# S0 = 100
# r = 0.05
# q = 0.01
# sigma = 0.5
# T = 0.6
# K = 90
