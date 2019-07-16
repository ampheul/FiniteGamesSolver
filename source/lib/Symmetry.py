from Permutation import Permutation

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
                **{'mapping' : tuple([self.mapping[i] for i in other.mapping]),
                'group' : group} )

    def equals(self, other):

        return hash(self) == hash(other)

    @classmethod
    def identity(cls, n, *arr, group, **kwargs):

        e = super().identity(n, *arr, group=group, **kwargs)

        e.group = group
        group.identity = e
        group.elements.add(e)

        return e
