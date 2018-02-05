
class Game:

    PI, PII = True, False
    WIN, LOSS = 1, 0

    def __init__(self, state, *arr, **kwargs):

        self.__state = state
        self.__subgames = {}
        self.currentPlayer = Game.PI

    @property
    def options(self):
        # generator function for options
        pass

    @property
    def value(self):

        try:

            return self.__value

        except AttributeError:

            value = self.options[0].value

            for option in self.options:

                if value < option.value:
                    # invert the ordering relation if PII
                    value = option.value if self.player is Game.PI else value

            self.__value = value

            return value


class SubGame:



class Domino(Game):

    def __init__(self, *arr, **kwargs):
