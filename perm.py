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

def base_board():
    return [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


X_VAL = 'X'
O_VAL = 'O'
CASE1 = deepcopy(base_board())
CASE1[0][0] = X_VAL

def gen_board(moves):
    board = base_board()
    for move in moves:
        player, r, c = move
        board[r][c] = player
    return board



class Cycle:
    def __init__(self, parent, my_way:list = False) -> None:
        self.parent = False
        self.way = deepcopy(my_way)
        self.branches = []
        self.has_won = False
        self.player_val = X_VAL if my_way[0][0] == O_VAL else O_VAL
        self.allow = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)} - {self.way[-1]}
        if parent:
            self.has_won = parent.has_won
            self.allow = parent.allow - {self.way[-1]}
            self.parent = parent
            self.way = deepcopy(self.parent.way)
            self.way.append(deepcopy(my_way))
            self.player_val = X_VAL if self.parent.player_val == O_VAL else O_VAL
        if len(self.allow):
            self.check_vicory()
        else:
            self.has_won = True

    def gen_game_state(self):
        board = base_board()
        
        for state in self.way:
            player, row_col = state
            row, col = row_col
            board[row][col] = player
        return board
    

    def generate_braches(self):
        if self.has_won:
            print("Can't generate new branches")
            return False
        
        for row_col in self.allow:
            self.branches.append(Cycle(self, (self.player_val, row_col)))
    
    def check_vicory(self):
        player = X_VAL if self.player_val == O_VAL else O_VAL
        if game_check(self.gen_game_state(), player):
            self.has_won = True
            return True
        return False
        
parent = [Cycle(False, [(X_VAL, (0, 0))])]
parent[0].generate_braches()
parent = parent[0].branches 

done = []
while len(parent):
    children = []
    for case in parent:
        case.generate_braches()
        children.extend(case.branches)
    parent = children
    i = 0
    while i < len(parent):
        if parent[i].has_won == True:
            done.append(parent.pop(i))
            i -= 1
        i += 1
    print(len(done))

#for case in done:
#    for n in case.gen_game_state()[::-1]:
#        print(n)
#    print("_____________")
import json
with open("test_dta.json", 'w') as f:
    json.dump([branch for branch in [case.gen_game_state() for case in done]], f)