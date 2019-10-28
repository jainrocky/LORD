import os, sys, warnings
    

def find_lcs(x, y, print_seq=None):
    n = len(x)
    m = len(y)
    cache = [ [0]*(m+1) for i in range(n+1) ]
    p_cache = [ ['']*(m+1) for i in range(n+1) ]
    for row in range(1, n+1):
        for col in range(1, m+1):
            if x[row-1] is y[col-1]:
                cache[row][col] = cache[row-1][col-1]+1
                p_cache[row][col] = '\\'

            else:
                if cache[row][col-1]>cache[row-1][col]:
                    cache[row][col], p_cache[row][col] = cache[row][col-1], '<'
                else:
                    cache[row][col], p_cache[row][col] = cache[row-1][col], '^'

    size = cache[row][col]
    seq = [''] * size
    i=n
    j=m
    while i > 0 and j > 0:
        if p_cache[i][j] == '\\':
            seq[size-1] = x[i-1]
            i, j, size = i-1, j-1, size-1
        elif p_cache[i][j] == '<':
            j -= 1
        else:
            i -= 1
    return ''.join(seq)

    
if __name__=='__main__':
    x='my name is rocky jain'
    y='and my name is rajat jain'
    print(find_lcs(x, y))
