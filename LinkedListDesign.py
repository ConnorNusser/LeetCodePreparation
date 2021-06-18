class Node:
    def __init__(self, val=None, nex=None):
        self.val = val
        self.nex = nex




class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        ct = 0
        var = self.head
        while(ct < index and var.nex != None):
            var = var.nex
            ct = ct + 1
        
        if(var.val == None):
            return -1
        
        return var.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        
        if self.head == None:
            self.head = Node(val)
        else:
            var1 = self.head
            self.head = Node(val)
            self.head.nex = var1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        last_element = self.head
        while(last_element.nex != None):
            last_element = last_element.nex
        last_element.nex = Node(val)
        
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        return_link = self.head
        head = self.head
        ct = 0
        while(ct < index - 1 and head.nex != None):
            head = head.nex
            ct = ct + 1
            
            
        if head.nex != None:
            end = head.nex
        else:
            return
        
        head.nex = Node(val, end)
        
        
        
        
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        
        
        if index == 0:
            self.Head = self.Head.next
            return 
        
        curr = self.head
        ct = 0
        while(index - 1 > ct):
            ct = ct + 1
            curr = curr.nex
        if curr.nex == None:
            return
        beforeCurr = curr
        deleteCurr = beforeCurr.nex
        curr = deleteCurr.nex
        beforeCurr.nex = curr
        
        
            
        
        
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
print("--------")
obj.deleteAtIndex(1)
obj.get(1)

car = obj.head

while(car != None):
    print(car.val)
    car=car.nex
