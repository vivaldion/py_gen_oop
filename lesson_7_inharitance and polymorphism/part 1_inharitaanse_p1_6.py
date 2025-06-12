class Counter:
    def __init__(self, start=0):
        self.value = start if start >= 0 else 0
        self.value = start

    def inc(self, n=1):
        self.value +=n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0 , limit=10):
        Counter.__init__(self, start)
        self.limit = limit


    def inc(self, n=1):
        Counter.inc(self, n)
        self.value = min(self.value, self.limit)

counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)