
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
 
    def reverseList(self):
        previous = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = previous

            previous = current

            current = next

        self.head = previous
 
    def insertNode(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    
    def checkPalindrome(self):
        if self.head == None:
            return True

        a = []
  
        first = self.head
        while first != None:
            a.append(first.data)
            first = first.next

        self.reverseList()
        first = self.head

        i = 0
        while first != None:
            if first.data != a[i]:
                return False
            first = first.next
            i += 1

        return True

if __name__ == '__main__':
  
    data = [1, 2, 3, 2, 1]
    print("orignal linked list is =",data)

    linkedList = LinkedList()

    for i in reversed(range(len(data))):
        linkedList.insertNode(data[i])

    if linkedList.checkPalindrome():
        print("The linked list is a palindrome linked list.")
    else:
        print("The linked list is not a palindrome linked list.")
