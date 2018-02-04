'''Permutation.py

Contains classes that I want to use to check symmetry of boards in board.py

In particular I build a class function in SymmetryGroup to generate D_8 and
Z_2xZ_2, which are the symmetries of an mxn board.
'''

class Permutation:
    '''a bijection from the set of n elements to itself.
    contains a list of n distinct integers in the range 0 to n-1
    permute() takes an element i and returns mapping[i]
    '''
    def __init__(self, mapping, **kwargs):

        self.mapping = tuple(mapping)

    def permute(self, i):

        return self.mapping[i]

    def compose(self, other):

        return Permutation(
            # tuple from list comprehension is the fastest in python 3.6
            mapping= tuple([self.mapping[i] for i in other.mapping]) )

    def pow(self, k):

        def power(i):
            for j in range(k):
                i = self.mapping[i]
            return i

        return Permutation( mapping= tuple([power(i) for i in self.mapping]) )

    def __getitem__(self, index):

        return self.mapping[i]

    def __mul__(self, other):

        return self.compose(other)

    def equals(self, other):

        return self.mapping == other.mapping

    def __eq__(self, other):

        return self.equals(other)

    def __hash__(self):

        '''hash

            returns the saved hash value
            sets it if it is unset'''

        try:

            return self.__hash

        except AttributeError:

            # mapping is a tuple, hash it
            self.hash = hash(self.mapping)

            return self.__hash

    @classmethod
    def identity(cls, n):

        return cls(mapping= range(n))

class Symmetry(Permutation):

    def __init__(self, group, **kwargs):

        super().__init__(**kwargs)

        self.group = group

        group.elements.add(self)



    def compose(self, other):

        key = (a, b)

        try:

            return group.table[key]

        except KeyError:

            group.table[key] = Symmetry(
                mapping= tuple([self.mapping[i] for i in other.mapping]),
                group = self.group )


    def equals(self, other):

        return hash(self) == hash(other)

class SymmetryGroup:
    '''A set of permutations

    intended to be used as a subgroup of S_n

    Symmetry equality relies on hashes, which looks wack, but its faster.
    which is the intent.
    '''
    def __init__(self):

        self.elements = set()
        self.table = {}

    @classmethod
    def d8(cls, n):

        self = cls()
        # s is the reflection across the vertical bisector of an nxn board
        s = Symmetry(
                mapping= tuple([m*i+j for i in range(n) for j in range(n)[::-1]]),
                group= self )
        # s.r is the composition of rotation and reflection
        # s.r is equal to the transpose on an nxn board
        # since s.r is the transpose, permute by s to get (s.s).r = r
        r = Symmetry(
                mapping= tuple([ s[n*j+i] for i in range(n) for j in range(n) ]),
                group=self)
        e = Symmetry.identity(n*n)

        # calculate the following
        # automatically adds them to elements
        (e,   r,   r.pow(2),   r.pow(3),
        s, s*r, s*r.pow(2), s*r.pow(3))



    # implement this one later
    # def z2xz2(self, m, n):
        # return
