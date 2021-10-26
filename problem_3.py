#A = ["...X..","....XX","..X..."]
A = ["....X..","X......",".....X.","......."]

class Position:
    def __init__(self,row,col):
        self.row = row
        self.col = col
    
    def equals(self,pos):
        if self.row == pos.row and self.col == pos.col:
            return True
        else:
            return False
    def if_exist_in(self,poitions):
        for pos in poitions:
            if self.equals(pos):
                return True
        return False

def move(state,row,col):
    if state == 0:
        col = col+1 
    elif state == 1:
        row = row +1
    elif state == 2:
        col = col - 1
    elif state == 3:
        row = row -1
    return Position(row,col)

def is_obsticle(arr,row,col):
    max_row = len(arr)-1
    max_col = len(arr[0])-1
    if row < 0 or row > max_row:
        return True
    elif col < 0 or col > max_col:
        return True
    elif arr[row][col] != ".":
        return True
    return False

def change_move_state(current_state):
    if current_state == 0:
        current_state = 1
    elif current_state == 1:
        current_state = 2
    elif current_state == 2:
        current_state = 3 
    elif current_state == 3:
        current_state = 0
    return current_state

def solution(A):
    current_position = Position(0,0)
    # 0 is Left to Right
    # 1 is Top to Bottom
    # 2 is Right to Lef
    # 3 is Bottom to Top
    move_state = 0
    cleaned_positions = []
    repeated_counter = 0
    while repeated_counter < 3:
        if is_obsticle(A,current_position.row,current_position.col):
            if len(cleaned_positions) > 0:
                current_position = cleaned_positions[len(cleaned_positions)-1]
            move_state = change_move_state(move_state)
        else:
            if not current_position.if_exist_in(cleaned_positions):
                cleaned_positions.append(current_position)
            else:
                repeated_counter = repeated_counter +1
        current_position = move(move_state,current_position.row,current_position.col)
    
    return len(cleaned_positions)

print(solution(A))