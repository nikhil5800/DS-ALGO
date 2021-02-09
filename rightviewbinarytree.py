class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def rightview(root):
    out = [0]
    level = 1
    return rightviewutil(out,root,level)
def rightviewutil(out,root,level):
    if root == None:
        return
    if level > out[0]:
        print('data is',root.val)
        out[0] = level
    rightviewutil(out,root.right,level+1)
    rightviewutil(out, root.left,level+1)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(5)
    root.left.left = Node(4)
    root.left.left.left = Node(6)
    rightview(root)
