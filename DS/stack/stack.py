import os, sys

class Stack:
    def __init__(self):
        self.curr=-1
        self.capacity=5
        self.stack=[None]*self.capacity
        
    def push(self, val):
        if self.curr+1 >= self.capacity:
            self.resize()
        self.curr += 1
        self.stack[self.curr] = val
        
    def pop(self,):
        if self.curr < 0:
            raise ValueError('stack is empty!')
        popped = self.stack[self.curr]
        self.stack[self.curr]=None
        self.curr -= 1
        return popped

    def top(self, ):
        return self.stack[self.curr]
    def resize(self, ):
        self.capacity <<= 1
        temp = [None]*self.capacity
        i=0
        while i<=self.curr:
            temp[i] = self.stack[i]
            i+=1
        self.stack=temp
         
    def empty(self, ):
        return self.curr == -1


if __name__=='__main__':
    s = Stack()
    s.push( 21 )
    s.push( 213 )
    s.push( 41 )
    s.push( 12 )
    s.push( 21 )
    s.push( 42 )
    s.push( 41 )
    s.push( 454 )
    s.push( 445 )
    s.push( 317 )

    while not s.empty():
        print(s.pop())
        
