from src.CRR_binomial_tree import TwoDimTree

S0 = 100
r = 0.05
q = 0.02
sigma = 0.5
T = 0.5
K = 90
n = 100

EuropeanCall = TwoDimTree(S0, K, r, q, sigma, T, n, "C", "E")
EuropeanPut = TwoDimTree(S0, K, r, q, sigma, T, n, "P", "E")
AmericanCall = TwoDimTree(S0, K, r, q, sigma, T, n, "C", "A")
AmericanPut = TwoDimTree(S0, K, r, q, sigma, T, n, "P", "A")

print(f"European Call value: {EuropeanCall.get_option_value()}")
print(f"European Put value: {EuropeanPut.get_option_value()}")
print(f"American Call value: {AmericanCall.get_option_value()}")
print(f"American Put value: {AmericanPut.get_option_value()}")

