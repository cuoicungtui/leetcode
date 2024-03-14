"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

from DataStructures.Queue import Queue
from DataStructures.Tree import Node, BinaryTree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def check_left(self):
        return self.left is None
    def check_right(self):
        return self.right is None
     
def serialize(node : Node) -> str:
    if node.check_left() and node.check_right():
        return node.val +';'+'None;'+ "None"

    if node.check_left() and not node.check_right():
        return node.val+ ';None;' +  serialize(node.right) 
    
    if not node.check_left() and node.check_right():
        return node.val+ ';' +  serialize(node.left)+ ";None"

    return node.val+ ';' +  serialize(node.left) + ';'+ serialize(node.right)


def deserialize_action(node : Node,queue : Queue)-> Node:

    if queue.__len__() == 0:
        return node
    left = queue.dequeue()
    if left != 'None':
        node.left = Node('left')
        node.left = deserialize_action(node.left,queue)

    if queue.__len__() == 0:
        return node
    right = queue.dequeue()    
    if right !='None':
        node.right = Node('right')
        node.right = deserialize_action(node.right,queue)
    
    return node

def deserialize(s : str)->Node:
    s = s.split(';')
    queue = Queue()

    for i in s:
        queue.enqueue(i)
    queue.dequeue()
    root = Node('root')
    return deserialize_action(root,queue)
    

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left')), Node('right',))
    print(serialize(deserialize('root;left;left;None;None;None;right;None;None'))) 



