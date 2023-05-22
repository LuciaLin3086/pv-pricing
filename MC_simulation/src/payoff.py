import numpy as np

# Calculate the option payoff of the simulated prices.
class Payoff:
    def __init__(self, K, which_option):
        self.K = K
        self.which_option = which_option

    def get_payoff(self, price):
        """
        this method is used to calculate the payoff from given underlying asset's price
        :param price : a float type
        :return payoff : a float type
        """
        if self.which_option == "C":
            payoff = max(price - self.K, 0)
        else:
            payoff = max(self.K - price, 0)

        return payoff

    def get_payoff_matrix(self, price_matrix):
        """
        this method is used to combine each payoff into a numpy array
        :param price_matrix : numpy array
        :return payoff_ls : numpy array
        """
        n, N = price_matrix.shape
        payoff_ls = []
        for row in range(n):
            payoff_ls.append([])
            for price in price_matrix[row, :]:
                payoff_ls[row].append(self.get_payoff(price))

        return np.array(payoff_ls)  # reshape to original shape n x N