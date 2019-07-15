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
    