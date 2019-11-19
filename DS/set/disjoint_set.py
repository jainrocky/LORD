import os, sys 

class DJSet:
    
    def __init__(self, n):
        self.sets = [-1]*n

    def find(self, s):
        root = self.sets[s]
        if root < 0:
            return s
        while root > 0 and self.sets[root] > 0:
            root = self.sets[root]
        return root

    def union(self, s1, s2):
        par_s1, par_s2 = self.find(s1), self.find(s2)
        if par_s1 is not par_s2:
            if self.sets[par_s1] <=  self.sets[par_s2]:
                self.sets[par_s1] += self.sets[par_s2]
                self.sets[par_s2] = par_s1
                
            else:
                self.sets[par_s2] += self.sets[par_s1]
                self.sets[par_s1] = par_s2

if __name__=='__main__':
    n=6
    djs = DJSet(n)
    print(djs.find(2))
    print(djs.find(5))
    djs.union(2, 5)
    print(djs.find(5))
        
