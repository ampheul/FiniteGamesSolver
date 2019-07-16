from Symmetry import Symmetry

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
    def identity(self):

        return self.__identity

    @identity.setter
    def identity(self, value):

        self.__identity = value