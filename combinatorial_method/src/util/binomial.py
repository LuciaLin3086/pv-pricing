from math import log, exp

def Binomial(n, p, j):
    sum = 0
    for i in range(1, n+1):
        sum += log(i)
    for i in range(1, j+1):
        sum -= log(i)
    for i in range(1, n-j+1):
        sum -= log(i)

    sum += (n-j) * log(p) + j * log(1 - p)

    return exp(sum)


if __name__ == "__main__":
    n = 100
    j = 1
    p = 0.5

    print(Binomial(n, p, j))


