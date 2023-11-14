from copy import deepcopy

# listiga operatsioonid
def trans(l):
    n = [[] for _ in l]
    for row in l:
        for i, val in enumerate(row):
            n[i].append(val)
    return n
def flip_v(l):
    for row in l:
        row.reverse()
    return l
def flip_h(l):
    l[0], l[-1] = l[-1], l[0]
    return l
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]#TESTIMISEKS

# KOntroll operats.
def vert_check(arr2d, win_val):
    for row in arr2d:
        if row.count(win_val) >= 3:
            return True
def cross_check(arr_2d, win_val):
    return arr_2d[0][0] == arr_2d[1][1] == arr_2d[2][2] == win_val
def game_check(arr_2d, win_val):
    return vert_check(arr_2d, win_val) or vert_check(trans(arr_2d), win_val) or cross_check(arr_2d, win_val) or cross_check(flip_v(arr_2d), win_val)


X_VAL = 1
O_VAL = -1

base_0 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

base_1 = deepcopy(base_0)
base_1[1][1] = X_VAL
base_2 = deepcopy(base_0)
base_2[0][1] = X_VAL
base_3 = deepcopy(base_0)
base_3[0][0] = X_VAL

def abc():
    a = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
    return a
#VB peab tegema vaid käikudega
#def cycle_mvs(done_mvs, illegal:set, player):
#    all_possible = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
#    possible = all_possible-illegal
#    dissallow = []
#    step = []
#    cln = []
#    print(possible)
#    for r_c in possible:
#        step.append()


def cycle(start_array, illegal, player):
    all_possible = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    possible = all_possible-set(illegal)
    dissallow = list(illegal)
    step = []
    for r_c in possible:
        row, col = r_c
        a = deepcopy(start_array)
        a[row][col] = player
        dissallow.append(r_c)
        step.append(a)
        del a
    return step, dissallow


def generate_moves(seed):
    seed = [deepcopy(seed)]
    moves, not_allow = 
    



def print(states, n):
    # TESTIMISEKS, printimine
    for i, state in enumerate(states):
        for row in state:
            print(row)
        print(n[i])
        print("--------------------")

def do(array2D):
    pass
