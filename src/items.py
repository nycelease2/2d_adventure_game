class knife:
    def __init__(self):
        self.damage = 5
        self.attkDist = 30
        self.weight = 1
        self.stackability = 1
    def obtain(player1):
        player1.inventory["knife"] = 1

class meat:
    def __init__(self):
        self.replenish = 5
        self.weight = 3
        self.stackability = 30
    def obtain(player1):
        player1.inventory["meat"] = 30

class pistol:
    def __init__(self):
        self.damage = 30
        self.attkDist = 200
        self.weight = 7
        self.stackability = 1
    def obtain(player1):
        player1.inventory["pistol"] = 1
