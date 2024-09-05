class User:
    def __init__(self, name, friends=0):
        self.name = name
        self.friends = friends

    def add_friends(self, n):
        self.friends += n

