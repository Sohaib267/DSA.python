class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
      
def create(head, x):
    temp = Node(x)
    ptr = head
    if(head is None):
        head = temp
    else:
        while(ptr.next is not None):
            ptr = ptr.next
        ptr.next = temp
      
    return head
  
def removeNthFromEnd(head, B):
    start = Node(-1)
    start.next = head
    fastPtr = start
    slowPtr = start
    for i in range(B):
        fastPtr = fastPtr.next
    while(fastPtr.next is not None):
        fastPtr = fastPtr.next
        slowPtr = slowPtr.next
      
    slowPtr.next = slowPtr.next.next
    return start.next
  
def display(head):
    temp = head
    while(temp is not None):
        print(temp.data, end=" ")
        temp = temp.next
      
head = None
head = create(head, 12)
head = create(head, 21)
head = create(head, 3)
head = create(head, 4)
head = create(head, 9)
  
n = 2
  
print("Linked list before modification: ")
display(head)
  
head = removeNthFromEnd(head, 2)
print("\nLinked list after modification: ")
display(head)