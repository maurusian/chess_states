def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def choice(n,m): #choice of n elements from m
    if n==m or n == 0:
        return 1
    elif n>m or n<0 or m<0:
        return 0
    elif n==1:
        return m
    else:
        ch = 1
        for i in range(m-n+1,m+1):
            ch*=i

        ch = ch/&factorial(n)
    return ch

def two_kings(dim): #dim = dimensions of the board, as tuple, with dim[0] being on the playing direction
    """
    Calculates the number of chess board states
    with the two kings only, given a board of
    dimensions dim[0] and dim[1].
    Keeping the board dimensions as a parameter
    is useful in calculating the number of chess
    board states when we have other pieces, since
    we can simply subdivide the board into different
    zones and call this function with different
    dimension values.
    """
    board_size = dim[0]*dim[1] #number of squares on the board
    card_m = board_size - 2*dim[0] - 2*dim[1] + 4 #number of squares of the board middle
    card_a1 = 4
    card_b = 2*dim[0] - 4
    card_a2 = 2*dim[1] - 4
    
    return choice(1,card_m)*choice(1,board_size-8-1)+choice(1,card_a1)*choice(1,board_size-3-1)+choice(1,card_b+card_a2)*choice(1,board_size-5-1)
        
def two_kgs_whi_pawns(X):
    cases = [0,0,0]
    #No king in A1 U A2
    cases[0] = choice(X,64-8-2)*two_kings((7,8))
    #One king in A1 U A2
    cases[1] = choice(X,64-8-1)*(choice(1,2)*choice(1,56-2)+choice(1,6)*choice(1,56-3))
    #Both kings in A1 U A2
    cases[2] = choice(X,64-8)*(choice(1,2)*choice(1,8-1-1)+choice(1,6)*choice(1,8-2-1))
    return sum(cases)

def two_kgs_all_pawns(X,Y):
    cases = [0,0,0,0,0]
    #No king in E = A1 U A2 U A1' U A2'
    cases[0] = two_kings((6,8))*choice(X,64-8-2)*choice(Y,64-8-X-2)
    #White king in A1 U A2 and black king not in E
    cases[1] = (choice(1,2)*choice(1,56-2)+choice(1,6)*choice(1,56-3))*choice(X,64-8-1)*choice(Y,64-8-2-X)
    #Black king in A1 U A2 and white king not in E
    cases[2] = (choice(1,2)*choice(1,56-2)+choice(1,6)*choice(1,56-3))*choice(Y,64-8-1)*choice(Y,64-8-2-Y)
    #Both kings in A1 U A2
    cases[3] = (choice(1,2)*choice(1,8-1-1)+choice(1,6)*choice(1,8-2-1))*choice(X,64-8)*choice(Y,64-8-X-2)
    #Both kings in A1' U A2'
    cases[4] = (choice(1,2)*choice(1,8-1-1)+choice(1,6)*choice(1,8-2-1))*choice(Y,64-8)*choice(X,64-8-Y-2)

    return sum(cases)
    

if __name__ == '__main__':
    tkings = choice(1,64-28)*choice(1,56-1)+choice(1,24)*choice(1,59-1)+choice(1,4)*choice(1,61-1)
    #two_kgs_whi_pawns = sum([])
    print(tkings)
    print(two_kings((8,8)))
    print(sum([two_kgs_whi_pawns(X) for X in range(0,9)]))
    print(sum([two_kgs_all_pawns(X,0) for X in range(0,9)]))
    
