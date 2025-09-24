class Tree:
    def __init__(self, value):
        self.value = value
        self.winner = -float('inf')
        self.children = []