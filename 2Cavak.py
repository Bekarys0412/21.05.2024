class Number:
    def __init__(self, Max):
        self.Max=Max
        self.max_Max = max(Max)
        print("Max san:", self.max_Max)
Max = (3, 5, 7, 2, 9, 10)
number = Number(Max)