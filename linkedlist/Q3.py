


from LLinterviewqs import LinkedList    # time complexity O(n) space complexity O(1)

def partition(ll, x):
    curNode = ll.head                                 # O(1)
    ll.tail = ll.head                                 # O(1)

    while curNode:                                    # O(n)
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head                    # O(1)
            ll.head = curNode
        else:
            ll.tail.next = curNode                    # O(1)
            ll.tail = curNode
        curNode = nextNode
    if ll.tail.next is not None:                      # O(1)
        ll.tail.next = None

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL,50)
print(customLL)