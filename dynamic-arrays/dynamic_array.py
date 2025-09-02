class DynamicArray():
    def __init__(self):
        self.capacity = 10
        self.sz = 0
        self.data = [None for i in range(self.capacity)]

    def resize(self, new_capacity):
        self.capacity = int(new_capacity)
        new_data = [None for i in range(self.capacity)]
        for i in range(self.sz):
           new_data[i] = self.data[i]

        self.data = new_data  

    def append(self, x):
        # Resize array if needed 
        if self.sz == self.capacity:
            self.resize(self.capacity * 2)

        self.data[self.sz] = x
        self.sz += 1

    def get(self, i):
        if i < 0 or i >= self.sz:
           raise IndexError()
        return self.data[i]

    def set(self, i, x):
        if i < 0 or i >= self.sz:
           raise IndexError()

        self.data[i] = x

    def size(self):
        return self.sz

    def pop_back(self):
        if self.sz == 0:
           raise IndexError()
        self.sz -= 1
        self.data[self.sz] = None

        if self.sz <= self.capacity / 4:
            self.resize(self.capacity / 2)

    def pop(self, i):
        if i < 0 or i >= self.sz:
            raise IndexError()
        ret = self.get(i)

        for k in range(i, self.sz-1):
            self.data[k] = self.data[k+1]

        self.sz -= 1
        self.data[self.sz] = None

        if self.sz <= self.capacity / 4:
            self.resize(self.capacity / 2)

        return ret
    
    def contains(self, x):
        for i in range(self.sz):
            if self.data[i] == x: return True
        return False

    def insert(self, i, x):
        if i < 0 or i > self.sz:
            raise IndexError()

        if self.sz == self.capacity:
            self.resize(self.capacity * 2)
        
        for k in range(i, self.sz):
            self.data[k+1] = self.data[k]

        self.data[i] = x
        self.sz += 1 

    def remove(self, x):
        for i in range(self.sz):
            if self.data[i] == x:
                self.pop(i)
                return i
        return -1

def run_tests():
    def test_get_set():
        d = DynamicArray()
        # Setup array with [0,1,2,3,4]
        for i in range(5):
            d.append(i)
        
        # Test get
        assert d.get(0) == 0, "get(0) should return 0"
        assert d.get(4) == 4, "get(4) should return 4"
        
        # Test set
        d.set(0, 10)
        assert d.get(0) == 10, "After set(0,10), get(0) should return 10"
        
        # Test error cases
        try:
            d.get(-1)
            assert False, "get(-1) should raise IndexError"
        except IndexError:
            pass
        
        try:
            d.get(5)
            assert False, "get(5) should raise IndexError"
        except IndexError:
            pass
        
        try:
            d.set(-1, 0)
            assert False, "set(-1,0) should raise IndexError"
        except IndexError:
            pass
        
        try:
            d.set(5, 0)
            assert False, "set(5,0) should raise IndexError"
        except IndexError:
            pass

    def test_append():
        d = DynamicArray()
        # Test append to empty array
        d.append(1)
        assert d.size() == 1, "Size should be 1 after append"
        assert d.get(0) == 1, "Element at 0 should be 1"
        
        # Test multiple appends
        d.append(2)
        d.append(3)
        assert d.size() == 3, "Size should be 3 after appends"
        assert d.get(1) == 2, "Element at 1 should be 2"
        assert d.get(2) == 3, "Element at 2 should be 3"


    def test_pop_back():
        d = DynamicArray()
        # Test pop from empty array
        try:
            d.pop_back()
            assert False, "pop_back() on empty array should raise IndexError"
        except IndexError:
            pass
        
        # Setup array with [1,2,3]
        d.append(1)
        d.append(2)
        d.append(3)
        
        # Test pop_back
        d.pop_back()
        assert d.size() == 2, "Size should be 2 after pop_back"
        try:
            d.get(2)
            assert False, "get(2) should raise IndexError after pop_back"
        except IndexError:
            pass

    def test_resize():
        d = DynamicArray()
        # Test initial capacity
        assert d.capacity == 10, "Initial capacity should be 10"
        
        # Test grow capacity
        for i in range(11):
            d.append(i)
        assert d.capacity == 20, "Capacity should double to 20"
        
        # Test shrink capacity
        for i in range(8):
            d.pop_back()
        assert d.capacity == 10, "Capacity should shrink back to 10"

    def test_pop():
        d = DynamicArray()
        # Setup array with [0,1,2,3,4]
        for i in range(5):
            d.append(i)

        # Test pop from middle
        assert d.pop(2) == 2, "pop(2) should return 2"
        assert d.size() == 4, "Size should be 4 after pop"
        assert d.get(2) == 3, "Element at 2 should now be 3"

        # Test pop from start
        assert d.pop(0) == 0, "pop(0) should return 0"
        assert d.size() == 3, "Size should be 3 after pop"
        assert d.get(0) == 1, "Element at 0 should now be 1"

        # Test pop from end
        assert d.pop(2) == 4, "pop(2) should return 4"
        assert d.size() == 2, "Size should be 2 after pop"

        # Test error cases
        try:
            d.pop(-1) 
            assert False, "pop(-1) should raise IndexError"
        except IndexError:
            pass

        try:
            d.pop(2)
            assert False, "pop(2) should raise IndexError"
        except IndexError:
            pass

    def test_contains():
        d = DynamicArray()
        # Test empty array
        assert not d.contains(1), "Empty array should not contain 1"

        # Setup array with [1,2,3]
        d.append(1)
        d.append(2)
        d.append(3)

        # Test positive cases
        assert d.contains(1), "Array should contain 1"
        assert d.contains(2), "Array should contain 2"
        assert d.contains(3), "Array should contain 3"

        # Test negative cases
        assert not d.contains(0), "Array should not contain 0"
        assert not d.contains(4), "Array should not contain 4"

    def test_insert():
        d = DynamicArray()
        # Test insert into empty array
        d.insert(0, 1)
        assert d.size() == 1, "Size should be 1 after insert"
        assert d.get(0) == 1, "Element at 0 should be 1"

        # Test insert at start
        d.insert(0, 0)
        assert d.size() == 2, "Size should be 2 after insert"
        assert d.get(0) == 0, "Element at 0 should be 0"
        assert d.get(1) == 1, "Element at 1 should be 1"

        # Test insert at end
        d.insert(2, 2)
        assert d.size() == 3, "Size should be 3 after insert"
        assert d.get(2) == 2, "Element at 2 should be 2"

        # Test insert in middle
        d.insert(1, 3)
        assert d.size() == 4, "Size should be 4 after insert"
        assert d.get(1) == 3, "Element at 1 should be 3"

        # Test error cases
        try:
            d.insert(-1, 0)
            assert False, "insert(-1, 0) should raise IndexError"
        except IndexError:
            pass

        try:
            d.insert(5, 0)
            assert False, "insert(5, 0) should raise IndexError"
        except IndexError:
            pass

    def test_remove():
        d = DynamicArray()
        # Test remove from empty array
        assert d.remove(1) == -1, "Remove from empty array should return -1"

        # Setup array with [1,2,2,3]
        d.append(1)
        d.append(2)
        d.append(2)
        d.append(3)

        # Test successful removes
        assert d.remove(1) == 0, "Remove should return index 0"
        assert d.size() == 3, "Size should be 3 after remove"
        assert d.get(0) == 2, "Element at 0 should be 2"

        assert d.remove(2) == 0, "Remove should return index 0"
        assert d.size() == 2, "Size should be 2 after remove"
        assert d.get(0) == 2, "Element at 0 should be 2"

        # Test remove non-existent element
        assert d.remove(4) == -1, "Remove non-existent should return -1"

    tests = [
        lambda: test_get_set(),
        lambda: test_append(),
        lambda: test_pop_back(),
        lambda: test_resize(),
        lambda: test_pop(),
        lambda: test_contains(),
        lambda: test_insert(),
        lambda: test_remove()
    ]
    
    for test in tests:
        test()


if __name__ == "__main__":
    run_tests()