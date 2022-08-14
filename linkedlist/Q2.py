


from LLinterviewqs import LinkedList    #time complexity O(n) space complexity O(1)

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head                                          # O(1)

    for i in range(n):                                          # O(n)
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:                                             # O(n)
        pointer1 = pointer1.next                                # O(1)
        pointer2 = pointer2.next                                # O(1)
    return pointer1

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))