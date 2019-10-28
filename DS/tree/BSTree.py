import os, sys, warnings

class BSTree:

    class Node:
        def __init__(self, key, extras=None):
            self.key = key
            self.extras = extras
            self.l = None
            self.r = None
            self.x=0
            self.y=0
    
    def __init__(self, nodes=None):
        self.root = None
        if nodes:
            for i, node in enumerate(nodes):
                if i==0:
                    self.root = node
                else:
                    self.add_node(node)
            
    def add_node(self, node):
        if not self.root:
            self.root=node
        else:
            self.add(par=self.root, leaf=node)

    def add(self, par, leaf):
        if leaf.key <= par.key and not par.l:
            par.l = leaf
        elif leaf.key > par.key and not par.r:
            par.r = leaf
        elif leaf.key <= par.key:
            self.add(par.l, leaf)
        elif leaf.key > par.key:
            self.add(par.r, leaf)

    def print(self):
        self._print(self.root)

    def _print(self, node):
        if not node:
            return
        print(node.key)
        self._print(node.l)
        self._print(node.r)

    def max_height(self):
        return self._height(self.root)-1

    def _height(self, par):
        if not par:
            return 1
        else:
            return max(self._height(par.l), self._height(par.r)) + 1

        
    def draw(self):
        warnings.warn('draw function required extra Modules such as numpy and matplotlib')
        try:
            import matplotlib.pyplot as plt
            import numpy as np
        except:
            raise ImportError

        def build_coords(par, l_bound, u_bound):
            if par.l:
                par.l.x = (par.x + l_bound) // 2 
                par.l.y = par.y - 20
                build_coords(par.l, l_bound, par.x)
            if par.r:
                par.r.x = (par.x + u_bound) // 2
                par.r.y = par.y - 20
                build_coords(par.r, par.x, u_bound)
        
        def _draw(par, ax):
            if par:
                plt.text(par.x-4, par.y+4, par.key)
                ax.add_artist(plt.Circle((par.x, par.y), 4, color=np.random.rand(3)))
                if par.l:
                    plt.plot([par.x, par.l.x], [par.y, par.l.y], color='r')
                if par.r:
                    plt.plot([par.x, par.r.x], [par.y, par.r.y], color='r')        
                _draw(par.l, ax)
                _draw(par.r, ax)

        max_h = self.max_height()
        
        build_coords(self.root, -max_h * 20, max_h * 20)

        ax = plt.gca()
        plt.axis('equal')
        ax.set_xlim((-max_h * 30, max_h * 30))
        ax.set_ylim((-max_h * 30, 100))
        
        _draw(self.root, ax)

        plt.show()
        
        
        

if __name__=='__main__':

    t = BSTree()
    t.add_node(BSTree.Node( 30 ))
    t.add_node(BSTree.Node( 10 ))
    t.add_node(BSTree.Node( 20 ))
    t.add_node(BSTree.Node( 40 ))
    t.add_node(BSTree.Node( 42 ))
    t.add_node(BSTree.Node( 32 ))
    t.add_node(BSTree.Node( 12 ))
    t.add_node(BSTree.Node( 145 ))
    t.add_node(BSTree.Node( 121 ))
    t.add_node(BSTree.Node( 131 ))
    t.add_node(BSTree.Node( 112 ))
    t.add_node(BSTree.Node( 165 ))
    t.add_node(BSTree.Node( 331 ))
    t.add_node(BSTree.Node( 134 ))
    t.add_node(BSTree.Node( 31 ))
    t.add_node(BSTree.Node( 33 ))
    t.add_node(BSTree.Node( 3 ))
    t.add_node(BSTree.Node( 41 ))
    t.add_node(BSTree.Node( 1 ))
    t.add_node(BSTree.Node( 14 ))
    t.add_node(BSTree.Node( 43 ))
    t.add_node(BSTree.Node( 12 ))
    t.add_node(BSTree.Node( 13 ))
    t.add_node(BSTree.Node( 23 ))
    t.add_node(BSTree.Node( 33 ))
    t.add_node(BSTree.Node( 76 ))
    t.add_node(BSTree.Node( 50 ))
    t.add_node(BSTree.Node( 5 ))
    t.add_node(BSTree.Node( 1 ))
    t.add_node(BSTree.Node( 22 ))
    t.add_node(BSTree.Node( 7 ))
    t.add_node(BSTree.Node( 32 ))
    
    t.print()
    t.draw()
        
        
