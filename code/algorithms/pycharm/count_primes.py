def countPrimes(n):
    if n < 2:
        return 0
    s = [1] * n  # mark all as prime
    s[0] = 0
    s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 1:  # starting with 2, saying it's prime
            for j in range(i * i, n, i):
                s[j] = 0
    return sum(s)

print(1e8)
print(countPrimes(int(1e8)))
