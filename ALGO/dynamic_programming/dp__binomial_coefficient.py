import os, sys


def ncr(n):
    cache = [ [1]*(n) for i in range(n) ]
    for i in range(n):
        for j in range(n):
            if i!=j and j!=0:
                cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
    return cache


if __name__=='__main__':
    table = ncr(11) # ncr upto 11c11
    print(table[4][2])
    print(table[5][4])
    print(table[5][2])
    print()
    for i, row in enumerate(table):
        print(*row[:i+1])
