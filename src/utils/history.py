class RollHistory:
    def __init__(self):
        self.history = []

    def add(self, roll_result):
        self.history.append(roll_result)

    def get_last(self, n=10):
        return self.history[-n:]
