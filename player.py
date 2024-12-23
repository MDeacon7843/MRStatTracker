class Player:


    names = []


    def __init__(self, ign: str) -> None:
        self.ign = None
        Player.names.append(ign)
        self.games = []
    

    def __str__(self):
        return "Player: " + self.ign
    

    def addGame(self, game: dict) -> None:
        self.games.append(game)