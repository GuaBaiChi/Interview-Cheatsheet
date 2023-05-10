class HashMap:
    def __init__(self):
        self.size = 10
        self.array = [None] * self.size

    def get(self, key: str) -> str:
        return self.array[hash(key) % self.size]

    def set(self, key: str, value: str) -> None:
        self.array[hash(key) % self.size] = value


# driver code
test = HashMap()
key = 1
value = "derp"
test.set(key, value)
test.set(2, "test")
print(test.get(1))
print(test.get(2))
print(test.get(3))
