from src.CRR_binomial_tree_better import OneDimTree

S0 = 100
r = 0.05
q = 0.02
sigma = 0.5
T = 0.5
K = 90
n = 100

EuropeanCall = OneDimTree(S0, K, r, q, sigma, T, n, "C", "E")
EuropeanPut = OneDimTree(S0, K, r, q, sigma, T, n, "P", "E")
AmericanCall = OneDimTree(S0, K, r, q, sigma, T, n, "C", "A")
AmericanPut = OneDimTree(S0, K, r, q, sigma, T, n, "P", "A")

print(f"European Call value: {EuropeanCall.get_option_value()}")
print(f"European Put value: {EuropeanPut.get_option_value()}")
print(f"American Call value: {AmericanCall.get_option_value()}")
print(f"American Put value: {AmericanPut.get_option_value()}")