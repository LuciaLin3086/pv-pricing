import scipy.stats as stats
from math import log, pow, sqrt, exp

# hyperparameter
S0 = 50
r = 0.1
q = 0.05
sigma = 0.4
T = 0.5
K = 50


def N(x):
    return stats.norm.cdf(x)  # normal cdf

class BS:

    def __init__(self, S0, r, q, sigma, T, K, C_P): # C_P: Calls or Puts
        self.S0 = S0
        self.r = r
        self.q = q
        self.sigma = sigma
        self.T = T
        self.K = K
        self.C_P = C_P

        self.d1 = (log(self.S0 / self.K) + (self.r - self.q + pow(self.sigma, 2) / 2) * self.T) / (
                    self.sigma * sqrt(self.T))
        self.d2 = self.d1 - self.sigma * sqrt(self.T)

    def option_value(self):
        if self.C_P == "C":
            value = self.S0 * exp(-self.q * self.T) * N(self.d1) - self.K * exp(-self.r * self.T) * N(self.d2)
        else:
            value = self.K * exp(-self.r * self.T) * N(-self.d2) - self.S0 * exp(-self.q * self.T) * N(-self.d1)

        return value


EuropeanCall = BS(S0, r, q, sigma, T, K, "C")
EuropeanPut = BS(S0, r, q, sigma, T, K, "P")

print(f"European Call Value : {EuropeanCall.option_value():.4f}")  # .4f取小數點後4位，float
print(f"European Put Value : {EuropeanPut.option_value():.4f}")





