class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        new_freq = self.freq.get(val, 0) + 1
        self.freq[val] = new_freq

        if new_freq not in self.group:
            self.group[new_freq] = []
        self.group[new_freq].append(val)

        if new_freq > self.max_freq:
            self.max_freq = new_freq

    def pop(self) -> int:
        value = self.group[self.max_freq].pop()
        self.freq[value] -= 1

        if not self.group[self.max_freq]:
            del self.group[self.max_freq]
            self.max_freq -= 1

        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
