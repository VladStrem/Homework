class IteratorTeam:

    def __init__(self):
        self.team = Team()
        self.junior_iter = iter(self.team.juniors)
        self.senior_iter = iter(self.team.seniors)

    def __next__(self):
        try:
            return next(self.junior_iter)
        except StopIteration:
            try:
                return next(self.senior_iter)
            except StopIteration:
                raise StopIteration


class Team:
    def __init__(self):
        self.juniors = ["JPlayer 1", "JPlayer 2", "JPlayer 3", "JPlayer 4", "JPlayer 5"]
        self.seniors = ["Player 1", "Player 2", "Player 3", "Player 4"]

    def __iter__(self):
        return IteratorTeam()


for x in Team():
    print(x)
