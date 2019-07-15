class SLLNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
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
            
            
            
class SLLClass:
    siz=0
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        return self.head is None
    
    def add_front(self,data):
        node=SLLNode(data)
        node.set_next(self.head)
        self.head=node
        size+=1
        
    def size(self):
        return size
    
    def search(self,data):
        if self.head is None:
            return 'LL is empty so the element cannot be searched'
        else:
            current=self.head
            
            while current is None:
                if current.get_data() == data:
                    return "Found the element"
                else:
                    current=current.get_next()
                    
        return "Element is not present in the list"
    
    def remove(self,data):
        if self.head is None:
            return 'List is empty. No nodes to remove'
        
        found=False
        current=self.head
        prev=None
        
        while not found:
            if current.get_data() == data:
                found = True
            else:
                prev = current.get_next()
                current = current.get_next()
                
        if prev is None:
            self.head=current.get_next()
        else:
            prev.set_next(current.get_next())
            
        