class DBDB:
     def __init__(self,f):
         self._storage = Storage(f)
         self._tree = Binarytree(self._storage)
    
    def __getitem__(self,key):
        pass