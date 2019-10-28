import os, sys, warnings
INT_MAX = 2**31

def find_all(pattern, text):
    m = len(pattern)
    n = len(text)
    pos=[]
    n_char = 256
    p_hash = 0
    t_hash = 0
    msb_w = 1
    for i in range(m-1):
        msb_w = ((msb_w % INT_MAX) * (n_char % INT_MAX)) % INT_MAX
    for i in range(m):
        t_hash = (((t_hash * n_char) % INT_MAX) + ord(pattern[i]) ) % INT_MAX
        p_hash = (((p_hash * n_char) % INT_MAX) + ord(pattern[i]) ) % INT_MAX

    for i in range(n-m):
        j=0
        if t_hash == p_hash:
            while j < m and text[i+j] == pattern[j]:
                j+=1
        if j == m:
            pos.append(i)
        t_hash = ( (t_hash - ( ord(text[i]) * msb_w) % INT_MAX ) * n_char + ord(text[i+m]) ) % INT_MAX
        
    return pos
            
    
if __name__=='__main__':
    
    with open('../../TEST_DATA/LOREM_IPSUM.txt') as f:
        t = f.read()

    p='ipsum'    
    ind = find_all(pattern=p, text=t)
    print(ind)
    for i in ind:
        print(t[i-2:i+len(p)+2])
            
            





            
