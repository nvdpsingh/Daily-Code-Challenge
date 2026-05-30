class MyHashSet:

    def __init__(self):
        self.set1 = set()

        

    def add(self, key: int) -> None:
        self.set1.add(key)

    def remove(self, key: int) -> None:
        self.set1.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.set1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)