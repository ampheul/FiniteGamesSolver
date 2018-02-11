'''Permutation.py

Contains classes that I want to use to check symmetry of boards in board.py

In particular I build a class function in SymmetryGroup to generate D_8 and
Z_2xZ_2, which are the symmetries of an mxn board.
'''

class Permutation:
    '''a bijection from the set of n elements to itself.
    contains a list of n distinct integers in the range 0 to n-1
    permute() takes an element i and returns self.mapping[i]

    instances of Permutation are hashable

    permutations are callable, so you can just write sigma(n) instead of
    sigma.permute(n)

    Permutation is also powerable using ** notation. I use a fast powering
    algorithm, so for integers greater than 3 or 4, it should be very fast.
    It also supports an inverse operation.
    '''
    def __init__(self, mapping, *arr, **kwargs):

        self.__mapping = tuple(mapping)
        self.__n = len(mapping)

    def permute(self, i):

        return self.mapping[i]

    def compose(self, other):

        return Permutation(
            # tuple from list comprehension is the fastest in python 3.6
            mapping= tuple([self.mapping[i] for i in other.mapping]) )

    def pow(self, k):
        '''fast power algorithm for powers of itself
        '''
        if k < 0: return self.inverse().pow(-k)

        product = self.identity(len(self))

        if k == 0: return product

        powered = self
        while k > 0:
            if k % 2 == 1:
                product = product * powered
            k  = k >> 1
            if k > 0:
                powered = powered * powered

        return product

    def inverse(self):
        '''returns the inverse permutation to self
        '''
        return Permutation(
                mapping=tuple( [ y for x,y in
                                    list(enumerate(self.mapping)).sort() ] )

    def __pow__(self, k):

        return self.pow(k)

    def __call__(self, index):

        return self.permute(index)

    def __mul__(self, other):

        return self.compose(other)

    def equals(self, other):

        return self.mapping == other.mapping

    def __eq__(self, other):

        return self.equals(other)

    def __len__(self):

        return len(self.__mapping)

    def __hash__(self):
        '''returns the saved hash value
        sets it if it is unset
        '''
        try:

            return self.__hash

        except AttributeError:

            # mapping is a tuple, hash it
            self.__hash = hash(self.mapping)

            return self.__hash

    @classmethod
    def identity(cls, n, *arr, **kwargs):

        return cls(mapping= tuple(range(n)), *arr, **kwargs)

    def __str__(self):

        return str(self.mapping)

    def __repr__(self):

        return str(self.mapping)

class Symmetry(Permutation):
    '''
    A version of permutation which relies on a hash map from the group it is
    within to do composition
    '''
    def __init__(self, *arr, group, **kwargs):

        super().__init__(*arr, **kwargs)

        self.group = group

        group.elements.add(self)

    def compose(self, other):

        key = (self, other)
        group = self.group

        try:

            return group.table[key]

        except KeyError:

            group.table[key] = Symmetry(
                mapping= tuple([self.mapping[i] for i in other.mapping]),
                group= group )

    def equals(self, other):

        return hash(self) == hash(other)

    @classmethod
    def identity(cls, n, *arr, group, **kwargs):

        e = super().identity(n, *arr, **kwargs)

        e.group = group
        group.identity = e
        group.elements.add(e)

        return e

class SymmetryGroup:
    '''A set of permutations

    intended to be used as a subgroup of S_n

    Symmetry equality relies on hashes, which looks wack, but its faster.
    which is the intent.
    '''
    def __init__(self, name='',**kwargs):

        self.elements = set()
        self.table = {}
        self.name = name

    @classmethod
    def d8(cls, n, *arr, **kwargs):

        self = cls(*arr, **kwargs)

        self.name = 'D_8({0}x{0} board)'.format(n)

        # s is the reflection across the vertical bisector of an nxn board
        s = Symmetry(
                mapping= tuple([ m*i+j for i in range(n)
                                            for j in range(n)[::-1] ]),
                group= self )

        # s.r is the composition of rotation and reflection
        # s.r is equal to the transpose on an nxn board
        # since s.r is the transpose, permute by s to get (s.s).r = r
        r = Symmetry(
                mapping= tuple([ s(n*j+i) for i in range(n)
                                                for j in range(n) ]),
                group= self )

        e = Symmetry.identity(n*n, self)

        # calculate the following
        # automatically adds them to elements

        (e,   r,   r*r,   r*r*r,
         s, s*r, s*r*r, s*r*r*r )

        return self

    @classmethod
    def z2xz2(cls, m, n, *arr, **kwargs):

        self = cls(*arr, **kwargs)

        self.name = 'Z_2xZ_2({0}x{1} board)'.format(m, n)

        # s_h mirror across the horizontal
        s_h = Symmetry(
            mapping= tuple([(m-i-1)*m+j for i in range(m) for j in range(n)]),
            group= self )

        # s_v mirror across the vertical
        s_v = Symmetry(
            mapping= tuple([i*m+(n-j-1) for i in range(m) for j in range(n)]),
            group = self )

        # group identity
        # automatically added as the groups identity
        e = Symmetry.identity(m*n, group= self)

        (e, s_h, s_v, s_h*s_v)

        return self

    def __str__(self):

        return  'Group elements:\n{0}\nGroup Table:\n{1}'.format(
                    self.elements, self.table )
    @property
    def identity():

        return self.__identity

    @identity.setter
    def identity(self, value):

        self.__identity = value

if __name__ == '__main__':

    import sys

    p = Permutation(mapping = [1,0,2,5,4,3,8,6,9,7])
    n = int(sys.argv[1])
    s = p.pow(n)
    m = int(sys.argv[2])
    G = SymmetryGroup.z2xz2(n, m)

    print(s)
    print(G)
