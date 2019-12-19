def hammingWeight(n):
    # return bin(n).count('1')

    count = 0
    while n != 0:
        count = count + n % 2
        n = n // 2
    return count

print(hammingWeight(1001))

print('done')