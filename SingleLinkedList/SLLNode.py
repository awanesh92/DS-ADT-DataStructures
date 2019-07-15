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
            