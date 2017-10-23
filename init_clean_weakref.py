from weakref import WeakValueDictionary


class Counter(object):
    """
    Warning: Due to the precarious circumstances under which __del__() methods are invoked, 
    exceptions that occur during their execution are ignored, and a warning is printed to sys.stderr instead. 
    Also, when __del__() is invoked in response to a module being deleted (e.g., when execution of the program is done), 
    other globals referenced by the __del__() method may already have been deleted. 
    For this reason, __del__() methods should do the absolute minimum needed to maintain external invariants.
    
    http://python-3-patterns-idioms-test.readthedocs.io/en/latest/InitializationAndCleanup.html
    """

    _isntances = WeakValueDictionary()
    
    @property
    def count(self):
        return len(self._isntances)

    def __init__(self, name):
        self.name = name
        self._isntances[id(self)] = self
        print(name, "created")

    def __del__(self):
        """ 
        This methods gets invoked even before the object gets deleted. 
        So its safe to compare self.Count against 1 instead of 0.
        """
        print(self.name, ' Deleted')
        if self.count == 1:
            print('Last Counter object deleted')
        else:
            print(self.count-1, ' objects remaining')
