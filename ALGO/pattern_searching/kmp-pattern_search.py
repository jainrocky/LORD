import os, sys, warnings


def find_all(pattern, text):
    m = len(pattern)
    n = len(text)
    pos=[]
    lps=[0]
    roll_back_ind = 0
    i=1
    '''Make Longest Proper prefix table'''
    while i < m:
        if pattern[i] == pattern[roll_back_ind]:
            roll_back_ind+=1
            lps.append(roll_back_ind)
            i += 1
        elif pattern[i] is not pattern[roll_back_ind] and roll_back_ind > 0:
            roll_back_ind = lps[roll_back_ind-1]
        elif roll_back_ind==0:
            lps.append(0)
            i += 1
    i=j=0
    while i < n:
        if text[i] == pattern[j]:
            i,j = i+1, j+1
        if j == m:
            pos.append(i-m)
            j = lps[m-1]
        if text[i] is not pattern[j]:
            if j > 0:
                j = lps[j-1]
            else:
                i = i+1
    return pos
            
    
if __name__=='__main__':
    
    with open('../../TEST_DATA/LOREM_IPSUM.txt') as f:
        t = f.read()

    p='ipsum'    
    ind = find_all(pattern=p, text=t)
    print(ind)
    for i in ind:
        print(t[i-2:i+len(p)+2])
            
            





            
