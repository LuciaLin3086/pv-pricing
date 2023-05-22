import numpy as np
from math import log, pow, sqrt

# Based on ln(S)~ND, draw samples to simulate stock price
class PriceSimulator:
    def __init__(self, N, n, S0, r, q, sigma, T):
        self.N = N
        self.n = n
        self.S0 = S0
        self.r = r
        self.q = q
        self.sigma = sigma
        self.T = T

    def price_simulate(self):
        normal_sample = np.random.randn(self.n, self.N)  # std normal 抽樣出 n*N matrix

        lnS = normal_sample * self.sigma * sqrt(self.T) \
              + log(self.S0) + (self.r - self.q - pow(self.sigma, 2) / 2) * self.T  # ln(ST)分配

        return np.exp(lnS)  # 抽樣後的stock price # 因為是矩陣，所以用np，而不是math