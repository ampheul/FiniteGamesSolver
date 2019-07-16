#!/usr/bin/python3
'''
The tic tac toe type game (TTTTG) is played on a 1xn board.
players take turns placing (x)s on the board. The first player to
get 3 in a row wins.

it is obvious that if you play within two adjacent squares of another x
that you will lose the game. The other player will play the third
x and get 3 in a row. Thus we can ignore all losing moves like this.

It should be easy to see that for any game adding or removing losing options 
does not change the value of the game. Hence it can be shown inductively that
a TTTTG of 1xn is equivalent to the normal play game of n sticks in a line where
players take turns removing a stick its two left and two right neighbors 
(if they exist).

The nim equivalency of this game is calculated below, and hence we can
determine the value of TTTTG_100. Proof by algorithm. Whoopee.

Takes a command line argument n, which is the highest value of ttttg_n to
computer nim equivalency for.
'''

# nim values for the tic tac toe type games of index n
ttttg_values = [0, 1, 1, 1, 2, 2]
def nim(n):
    '''
    Get the nim value for ttttg_n
    ttttg_values is the array of nim values for games of 1xn 
    where n is the index where the value is stored
    ''' 
    if n < len(ttttg_values):
        return ttttg_values[n]
    raise Exception("out of value bounds")

def nim_options(n):
    '''
    Calculate all the options for ttttg_n in terms of nim equivalence
    return them as a set
    '''
    # a game of size 0 clearly has no options
    if n == 0:
        return {}
                
    # convert options into a set
    option_set = options(n)
    
    nim_option_set = { nim_sum([nim(x) 
                        for x in option]) 
                            for option in option_set }
    
    return nim_option_set

def options(n):
    '''
    returns a set of tuples. 
    each tuple sums to a subgame of ttttg_n
    each element of a tuple is an integer i which represents ttttg_i
    '''
    # the below algorithm does not work for the first few ttttg_n values
    # hence, return a prewritten list of the options
    if n in {0, 1, 2, 3, 4, 5}:
        
        return  [
            {}, 
            {(0,)}, 
            {(0,)}, 
            {(0,)}, 
            {(1,), (0,)}, 
            {(2,), (1,), (0,)}
        ][n]

    splitting_options = { (n-5-x, x) for x in range(int((n-5)/2+1)) }
    non_splitting_options = {(n-4,), (n-3,), (n-5,)}
    
    # the options include options which split the board in two, 
    # and those that do not
    return splitting_options | non_splitting_options

def nim_sum(nim_values_iterable):
    '''
    takes an iterable of nim values and returns the xor of all the elements
    '''
    sum = 0

    for element in nim_values_iterable:
        sum = sum ^ element

    return sum

def mex(nim_value_set):
    '''
    Calculate the minimal excludant from a set of nim values
    '''
    sorted_values = list(nim_value_set)
    sorted_values.sort()
    
    for i in range(len(sorted_values)):

        if sorted_values[i] != i:

            return i
    # if all nim values up to its size are in our nim_value_set then
    # it is equivalent to the nim value with those options
    return len(sorted_values)

def winning_move(subgame):
    '''
    given an option of a game, determine the winning move
    using nim equivalence. Subgames are tuples of sub-ttttg
    '''
    winning_moves = []
    for i in range(len(subgame)):
        
        for option in options(subgame[i]):
        
            subsubgame = subgame[:i] + option + subgame[i+1:]
            
            if nim_sum([nim(x) for x in subsubgame]) == 0:
            
                winning_moves.append(subsubgame)
    
    return winning_moves

if __name__ == '__main__':
    
    import sys

    # the maximum size of board to be played on 
    n = int(sys.argv[1])

    # populate the ttttg_values
    for i in range(6,n+1):

        ttttg_values.append( mex(nim_options(i)) )
    
    #print out ttttg_i along with its nim equivalency
    for i in range(len(ttttg_values)):
    
        print("%3d | %2d" % (i, ttttg_values[i]) )

    
    # print out values of ttttg_n organized by nim equivalency
    organized_by_nim_value = []
    
    for i in range(n+1):
    
        if len(organized_by_nim_value) <= nim(i):
    
            organized_by_nim_value.append([i])
    
        else:
    
            organized_by_nim_value[nim(i)].append(i)
    
    for i in range(len(organized_by_nim_value)):
    
        print('%3d: %s' % (i, str(organized_by_nim_value[i])))
    
    
    print("Tell me a move, and I will show you a list of winning moves. " 
          "type '()' to exit.") 
    
    from ast import literal_eval as make_tuple
    
    game = make_tuple(str(input('Enter a game tuple: ')))
    
    while len(game) > 0:
        def make_bundles(x):
            ''' Make bundles of sticks, as in the stick removing game
            which is equivalent to ttttg. You can also transfer a move in the
            stick game to ttttg_n and vice versa
            '''
            bundles = ['|'*i for i in x]
            return ' '.join(bundles)

        print('Winning moves for %s: \n%s' % ( 
                str(game), 
                '\n'.join([make_bundles(x)+'\n'+ str(x) 
                            for x in winning_move(game)]) 
                ) )
        game = make_tuple(input('Enter a game tuple: '))

    print('cya!')

