class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name}: {self.score}"
    
    @classmethod
    def comparator(cls, a, b):
        value = Player._compare_scores(a, b)
        if value != 0:
            return value
        else:
            return Player._compare_names(a, b)

    @classmethod
    def _compare_scores(cls, a, b):
        if a.score == b.score:
            return 0
        if a.score > b.score:
            return -1
        else:
            return 1

    @classmethod
    def _compare_names(cls, a, b):
        if a.name == b.name:
            return 0
        if a.name > b.name:
            return 1
        else:
            return -1