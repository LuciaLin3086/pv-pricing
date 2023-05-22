import numpy as np
from math import exp, sqrt, pow

from util.binomial import Binomial

# hyperparameter
S0 = 100
r = 0.05
q = 0.02
sigma = 0.5
T = 0.5
K = 90
n = 100

class CombinatorialＭethod:
    def __init__(self, S0, K, r, q, sigma, T, n, C_P):
        self.S0 = S0
        self.K = K
        self.r = r
        self.q = q
        self.sigma = sigma
        self.T = T
        self.n = n
        self.C_P = C_P

        self.delta_T = self.T / self.n
        self.u = exp(self.sigma * sqrt(self.delta_T))
        self.d = exp(- self.sigma * sqrt(self.delta_T))
        self.p = (exp((self.r - self.q) * self.delta_T) - self.d) / (self.u - self.d)


    def get_price(self, time, down_steps):
        price = self.S0 * pow(self.u, time - down_steps) * pow(self.d, down_steps)
        return price

    def get_payoff(self, price):
        if self.C_P == "C":
            payoff = max(price - self.K, 0)
            return payoff
        else:
            payoff = max(self.K - price, 0)
            return payoff

    def get_maturity_payoff(self):
        maturityPayoff_ls = []
        for down_steps in range(0, self.n + 1):
            maturityPayoff_ls.append(self.get_payoff(self.get_price(self.n, down_steps)))
            # maturityPrice = self.get_price(self.n, down_steps)
        return np.array(maturityPayoff_ls)

    def get_option_value(self):
        maturity_payoff = self.get_maturity_payoff()
        sum = 0
        for i in range(0, self.n+1):
            sum += maturity_payoff[i] * Binomial(self.n, self.p, i)
        return exp(-self.r * self.T) * sum



EuropeanCall = CombinatorialＭethod(S0, K, r, q, sigma, T, n, "C")
EuropeanPut = CombinatorialＭethod(S0, K, r, q, sigma, T, n, "P")

print(f"European Call value: {EuropeanCall.get_option_value()}")
print(f"European Put value: {EuropeanPut.get_option_value()}")



