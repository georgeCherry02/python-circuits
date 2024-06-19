class Source:
    def __init__(self):
        self.state = True

    def inverse(self):
        self.state = not self.state

    def high(self) -> bool:
        return self.state
