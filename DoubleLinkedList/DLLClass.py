class DLLNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
    def __repr__(self):
        return 'The data of the LL is {}'.format(self.data)
    
    def get_data(self):
        return self.data
    
    def set_data(self,ndata):
        self.data=ndata
        
    def get_next(self):
        return self.next
    
    def set_next(self,nnext):
        self.next=nnext
            
    def get_prev(self):
        return self.prev
    
    def set_prev(self,nprev):
        self.prev=nprev
    
class DLLClass:
    def __init__(self,data):
        self.head = None
    
    def __repr__(self):
        return 'Double Linked List data is ',format(self.head)
    
    def isEmpty(self):
        return self.head is None
    
    def size(self):
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def search(self,data):
        if self.head is None:
            return "LL is empty so the element cannot be searched."

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False
    
    def add_front(self,data):
        temp=DLLNode(data)
        temp.set_next(self.head)
        
        if self.head is not None:
            self.head.set_prev(temp)
        self.head = temp
        
        
    def remove(self,data):
        
        current = self.head
        found = False
        
        while not found:
        
            if current.get_data == data:
                found = True
            else:
                if current.get_next is None:
                    return 'Element is not present in the list'
                else:
                    current = current.get_next()
                    
        if current.prev is None:
            self.head = current.get_next()
        else:
            current.prev.set_next(current.get_next())
            current.next.set_prev(current.prev)
