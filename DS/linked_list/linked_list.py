import os, sys


class LinkedList:
    class Node:
        def __init__(self, val):
            self.data=val
            self.next=None
        def __str__(self, ):
            return str(self.data)
        
    def __init__(self, ):
        self.len=0
        self.head=None
    
    def push_front(self, val):
        if self.head is None:
            self.head=self.tail=self.Node( val )
        else:
            temp=self.Node( val )
            temp.next=self.head
            self.head=temp
        self.len+=1

    def push_back(self, val):
        if self.head is None:
            self.head=self.tail=self.Node( val )
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=self.Node( val )
        self.len+=1

    def pop_front(self, ):
        if self.head is not None and self.head.next is not None:
            r=self.head.data
            self.head=self.head.next
            self.len-=1
            return r
        elif self.head is not None:
            r=self.head.data
            self.head=None
            self.len-=1
            return r
        else:
            print('List is Empty!')
            
            
    def pop_back(self, ):
        if self.head is not None and self.head.next is not None:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            r=temp.next.data
            temp.next=None
            self.len-=1
            return r
        elif self.head is not None:
            r = self.head.data
            self.head=None
            self.len-=1
            return r
        else:
            print('List is Empty!')
            
    def is_contain(self, val):#search
        pass

    def push_at(self, index):
        pass
            
    def empty(self, ):
        return self.head is None
            
    def __iter__(self, ):
        temp=self.head
        while temp is not None:
            yield temp.data
            temp=temp.next

    def __len__(self, ):
        return self.len

    def __str__(self, ):
        return str(list(self))


# Examples
if __name__=='__main__':
    ll = LinkedList()
    for i in range(10, 0, -1):
        ll.push_back( i )
        
    print('list_print:', ll)
    print('loop_print:', end=' ')
    for l in ll:
        print(l, end=' ')
    print()
    print('pop_print:', end=' ')
    while not ll.empty():
        print(ll.pop_front(), end=' ')
    print()
    
