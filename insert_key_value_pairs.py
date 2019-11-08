import binary_tree
import argparse
import avl.py



if __name__ == '__main__':
    

    
     for l in open(sys.argv[1]):
        if sys.argv[2] == 'hash':
            print(h_ascii_sum(l, 10000))
        elif sys.argv[2] == 'AVL':
            print(AVLnode(l, 10000))
        elif sys.argv[2] == 'tree':
            print(Node(l, 10000))