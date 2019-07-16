import typing 
'''Permutation.py

A hashable callable permutation, takes a mapping and returns a 
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
            mapping= tuple([self.__mapping[i] for i in other.__mapping]) )

    def pow(self, k):
        '''fast power algorithm for powers of itself
        '''
        if k < 0: 
            return self.inverse().pow(-k)
        elif k == 0:
            return self.identity(len(self))
        else:
            product = self
            powered = self
            # primitive loop faster than recursion
            while k > 0:
                if k & 1:
                    product = product * powered

                powered = powered * powered
                k  = k >> 1

            return powered

    def inverse(self):
        '''returns the inverse permutation to self
        '''
        snd = lambda t: t[1] # for sorted, extract sort key
        return Permutation(mapping=
            tuple([ y for x,y in sorted(enumerate(self.mapping), key=snd) ]) )

    def __pow__(self, k):
        return self.pow(k)

    def __call__(self, index):

        return self.permute(index)

    def __mul__(self, other):

        return self.compose(other)

    def equals(self, other):

        return self.__mapping == other.__mapping

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
            self.__hash = hash(self.__mapping)

            return self.__hash

    @classmethod
    def identity(cls, n, *arr, **kwargs):
        print(repr(cls))
        return cls(mapping= tuple(range(n)), *arr, **kwargs)

    def __str__(self):

        return "Permutation" + str(self.__mapping)


if __name__ == '__main__':

    import sys

    a = Permutation(mapping = [1,0,2,5,4,3,8,6,7,9])#type: Permutation
    b = Permutation(mapping = [1,0,2,5,4,3,8,6,9,7])#type: Permutation
    print((a*b*b*b)**2)
    c = {
        a : "asdf",
        b : "drsda"
    }
    print(c)
