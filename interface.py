class DBDB:
     def __init__(self,f):
         self._storage = Storage(f)
         self._tree = Binarytree(self._storage)
    
     def __getitem__(self,key):
        self._assert_not_locked()
        self._tree.get()
    
     def _assert_not_locked(self):
        if self._storage.closed:
            raise ValueError('Database Closed !')
     def __setitem__(self, key, value):
         pass
     
     def commit(self):
         pass
        