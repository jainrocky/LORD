import os, sys, warnings, random
sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', 'DS', 'linked_list' ) )
from linked_list import LinkedList

def merge_sort(ll, reverse=None):
    if reverse is True:
        condition = lambda a, b: a>=b
    else:
        condition = lambda a, b: a<=b
    def find_mid(head, ):
        helper = head.next
        finder = head
        while helper is not None:
            helper=helper.next
            if helper is not None:
                finder=finder.next
                helper=helper.next
        return finder
    def merge(left, right):
        h1, h2 = left.head, right.head
        ll = LinkedList()
        while h1 is not None and h2 is not None:
            if condition(h1.data, h2.data):
                ll.push_back(h1.data)
                h1=h1.next
            else:
                ll.push_back(h2.data)
                h2=h2.next
        while h1 is not None:
            ll.push_back(h1.data)
            h1=h1.next
        while h2 is not None:
            ll.push_back(h2.data)
            h2=h2.next
        return ll
    def _sort(head):
        if head is not None and head.next is not None:
            t = find_mid(head)
            mid = t.next
            t.next=None
            left_ll = _sort(head)
            right_ll = _sort(mid)
            ll = merge(left_ll, right_ll)
            return ll
        elif head is not None:
            ll = LinkedList()
            ll.push_back(head.data)
            return ll
    return _sort(ll.head)



if __name__=='__main__':
    ll=LinkedList()
    n = 10
    item=[None]*n
    for i in range(n):
        ll.push_back(round(random.random()*100, 2))
    print(merge_sort(ll, reverse=True ))
    
    
