
#create binary tree (linked list)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

#preorder traversal of binary tree (linked list)
#start on the left-side node and go to the right-side node.

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

"""
preOrderTraversal(newBT)
print('\n\n')
"""

#inorder traversal of binary tree (linked list)
#start left-side at the left-side leaf then traverse right

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
"""
inOrderTraversal(newBT)
print('\n\n')
"""

#postorder traversal of binary tree (linked list)
#visit left-side leaf then left subtree, right subtree, then rootnode.

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
"""
postOrderTraversal(newBT)
print('\n\n')
"""

#levelorder traversal of binary tree (linked list)
#visit first level, second level, third level, etc.....last level
# N1 - N2 -N3 -N4 -N5 -N6 -N7 -N8 - N10

import Qlinkedlist as queue

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

"""
levelOrderTraversal(newBT)
"""
#search method for binary tree (linked list)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "THe BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

"""
print(searchBT(newBT, "Cola"))
"""

#INSERT A NODE IN BINARY TREE (linked list)

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"

"""
newNode = TreeNode("Cola")
print(insertNodeBT(newBT, newNode))
levelOrderTraversal(newBT)
"""

#delete a node from binary tree (linked list)

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild) 
        deepestNode = root.value
        return deepestNode

"""
deepestNode = getDeepestNode(newBT)
print(deepestNode.data)
"""

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

"""
newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newNode)
levelOrderTraversal(newBT)
"""


def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT doesn not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"

"""
deleteNodeBT(newBT, 'Hot')
levelOrderTraversal(newBT)
"""

#delete entire binary tree (linked list)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"

deleteBT(newBT)
levelOrderTraversal(newBT)