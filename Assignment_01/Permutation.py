'''Permutation.py

Contains classes that I want to use to check symmetry of boards in board.py

In particular I build a class function in SymmetryGroup to generate D_8 and
Z_2xZ_2, which are the symmetries of an mxn board.
'''

class Permutation:
    '''a bijection from the set of n elements to itself.
    contains a list of n distinct integers in the range 0 to n-1
    permute() takes an element i and returns map[i]
    '''
    def __init__(self, mapping, nocopy=False, **kwargs):

        if nocopy:
            self.mapping = kwargs['mapping']
        else:
            self.mapping = list(kwargs['mapping'])

    def permute(self, i):

        return self.mapping[i]

    def compose(self, other):

        return Permutation( mapping= map(self.permute, other.mapping),
                            nocopy= True)

    def pow(self, k):

        def power(i):
            for j in range(k):
                i = self[i]
            return i

        return Permutation( mapping= map(power, self.mapping),
                            nocopy = True)

    def __getitem__(self, index):

        return self.permute(i)

    def __mul__(self, other):

        return self.compose(other)

    def equals(self, other):

        return self.mapping == other.mapping

    def __eq__(self, other):

        return self.equals(other)

    @classmethod
    def identity(cls, n):

        return cls(mapping= range(n), nocopy=True)

class Symmetry(Permutation):

    def __init__(self, symbol, group, **kwargs):

        self.symbol = symbol
        self.group = group

        group.elements.add(self)

        super().__init__(**kwargs)

    def compose(self, other):

        return group.compose(self, other)

    def equals(self, other):

        try:

            return self.symbol == other.symbol

        except AttributeError:

            return self.mapping == other.mapping

    @classmethod
    def identity(cls, n, **kwargs):

        return cls(mapping= range(n), nocopy=True, **kwargs)

classj SymmetryGroup:
    '''A set of permutations

    intended to be used as a subgroup of S_n
    '''
    def __init__(self):

        self.elements = set()
        self.table = {}

    def compose(self, a, b):
        # search the pair in the table
        key = (a.symbol, b.symbol)

        try
            return self.table[key]

        except KeyError

            permutation = Permutation.compose(a, b)

            for sigma in self.elements:

                if permutation.mapping == sigma.mapping:

                    self.table[key] = sigma
                    return sigma
            else:
                # just generate the new symmetry, and return it
                self.table[key] = Symmetry(
                                    mapping= permutation.mapping,
                                    nocopy= True,
                                    symbol= a.symbol + b.symbol,
                                    group= self)

                return self.table[key]

    @classmethod
    def d8(cls, n):

        self = cls()
        # s is the reflection across the vertical bisector of an nxn board
        sMap = []

        for i in range(n):
            sMap += range(i*n,(i+1)*n)[::-1]

        s = Symmetry(symbol= 's', group = self, mapping= sMap, nocopy= True)

        rMap = []

        for i in range(n):

            for j in range(n):

                # s.r is the composition of rotation and reflection
                # it is equal to the transpose on an nxn board
                # since s.r is the transpose, permute by s to get (s.s).r = r

                srPermute = j*n + 1
                rMap.append( s.permute(srPermute) )

        r = Symmetry(mapping= rMap, nocopy= True)
        e = Symmetry.identity(symbol='')

        # calculate the following
        # automatically adds them to elements
        {e,   r,   r.pow(2),   r.pow(3),
        s, s*r, s*r.pow(2), s*r.pow(3)}

        for a in self.elements:
            for b in self.elements:
                key = (a, b)
                try:
                    self.elements[key]
                except KeyError:


    # implement this one later
    # def z2xz2(self, m, n):
        # return
