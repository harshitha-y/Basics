class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head=None
    def InsertAtFront(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
    def InsertAtEnd(self,data):
        node=Node(data)
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node
    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def InsertAtIndex(self, data, i):
        #print("Test",self.head.data)   --checking the position of head
        if self.head == None:           # edit for i=1
            print("linked list is empty")
        else:
            if i == 0:
                print("invalid number")
            else:
                temp = self.head
                node = Node(data)
                flag = False
                
                for i in range (2,i):
                    if(temp.next == None):
                        print("Index out of bounds")
                        flag = True
                        break
                    temp = temp.next
                if flag == False:
                    node.next=temp.next
                    temp.next=node
    
              
            
list1 =  LinkedList()
list1.InsertAtFront(10)
list1.InsertAtFront(20)
list1.InsertAtEnd(30)
list1.InsertAtIndex(40,2)
list1.InsertAtIndex(5,3)
list1.Display()



