class LogicalBase:
    def get(self,key):
        if not self._storage.locked:
            self._refresh_tree_ref()
        
        return self._get(self._follow(self._tree_ref), key)
    def set(self):
        pass
    def insert(self):
        pass
    def commit(self):
        pass