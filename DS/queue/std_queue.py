import os, sys, warnings

class Queue:
    def __init__(self, data=None):
        self.top=-1
        self.queue=[]
        self.size=0
        if data is not None:
            if isinstance(data, (list, )):
                self.queue=data
                self.top=0
                self.size=len(data)
            else:
                raise ValueError("'data' is must be a list of values")

    def push(self, val):
        self.queue.append( val )
        self.size+=1
        if self.top == -1:
            self.top += 1
    
    def pop(self):
        if self.top is not -1 and self.size > 0:
            r=self.queue[self.top]
            self.top+=1
            self.size-=1
            return r
        else:
            raise ValueError('Queue is empty!')

    def front(self):
        return self.queue[self.top]
    
    def empty(self):
        return self.size == 0

    def __str__(self, ):
        return str(self.queue[self.top: self.size])
    
   
if __name__=='__main__':
    data = [1, 2, 112, 4125, 253, 67, 23, 9, 29, 68, 457]
    q=Queue(data=data)
    q.push(21324)
    q.push(-123)
    q.push(-13)
    q.push(-90)
    
    while not q.empty():
        print(q.pop())
    
