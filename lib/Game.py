
class Game:
    '''
    Holds the instance vars of some arbitrary game, like the rules and
    a set hash map for subgames
    '''

    PI, PII = 1, 2
    WIN, LOSS = 1, 0

    def __init__(self, state, *arr, root=None, parent, **kwargs):

        self.state = state
        self.subgames = set(self)
        self.__currentPlayer = Game.PI
        self.__root = root
        self.parent = parent
        self.options = set()

        if parent is not None:



    @property
    def parent(self):

        return self.__parent

    @parent.setter
    def parent(self, val):
        self.__parent = val



    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, val):
        self.__state = val

    @property
    def options(self, subgame):
        # generator function for options
        return self.__options
    @options.setter
    def options(self, val):

        self.__options = set(val)

    @property
    def value(self):

        try:

            return self.__value

        except AttributeError:

            try:
                value = next(self.options).value

                for option in self.options:

                    if value < option.value:
                        # invert the ordering relation if PII
                        value = option.value if self.player is Game.PI else value

            # StopIteration raised if there are no options
            except StopIteration:

                value = Game.WIN if self.player == Game.PII else Game.LOSS

            self.__value = value

            return self.__value
