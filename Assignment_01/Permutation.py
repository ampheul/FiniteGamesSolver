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

        return Permutation( mapping= map(power, self.mapping),
                            nocopy = True)

    def __getitem__(self, index):

        return self.permute(i)

    def __mul__(self, other):
        return self.compose(other)

    def __eq__(self, other):
        return self.mapping == other.mapping

    @classmethod
    def identity(cls, n):
        return cls(mapping= range(n), nocopy=True)


class Symmetry(Permutation):

    def __init__(self, symbol, group, **kwargs):

        self.symbol = symbol
        self.group = group

        super().__init__(**kwargs)

    def compose(self, other):
        return group.compose(self, other)
    def __eq__(self, other):
        try:
            return self.symbol == other.symbol
        except AttributeError:
            return super().__eq__(self, other)
    @classmethod
    def identity(cls, n, mapping, nocopy, **kwarrgs):
        return cls(mapping= range(n), nocopy=True, **kwargs)

class SymmetryGroup:
    '''A set of permutations

    intended to be used as a subgroup of S_n
    '''
    def __init__(self):

        self.permutations = set()
        self.table = {}

    def compose(self, a, b):
        # search the pair in the table
        key = (a.symbol, b.symbol)

        if key in self.table:
            return self.table[key]
        else:
            permutation = Permutation.compose(a, b)
            if permutation in self.permutations:
                self.table[key] = Symmetry(
                                    mapping= permutation.compose(a, b).mapping,
                                    nocopy= True,
                                    symbol= a.symbol + b.symbol,
                                    group= self)

    @classmethod
    def d8(cls, n):

        self = cls()
        # s is the reflection across the vertical bisector of an nxn board
        sMap = []
        for i in range(n):
            sMap += range(i*n,(i+1)*n)[::-1]

        s = Symmetry(symbol= 's', mapping= sMap, nocopy= True)

        rMap = []

        for i in range(n):
            for j in range(n):
                # s.r is the composition of rotation and reflection
                # it is equal to the transpose on an nxn board
                # since s.r is the transpose, permute by s to get (s.s).r = r
                srPermute = j*n + 1
                rMap.append( s.permute(srPermute) )

        r = Permutation(mapping= srMap, nocopy= True)

        e = Symmetry.identity()
        self.permutations = [
            e,   r,   r.pow(2),   r.pow(3),
            s, s*r, s*r.pow(2), s*r.pow(3)
        ]

        for a in self.permutations:
            for b in self.permutations:
                key =

    def z2xz2(self, m, n):
