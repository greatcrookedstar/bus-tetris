import random

def remove_random_passengers(board, count=3):
    occupied = []
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell is not None:
                occupied.append((x, y))
                
    selected = random.sample(
        occupied, min(count, len(occupied))
    )
    
    for x, y in selected:
        board[y][x] = None
    return len(selected)

def remove_selected_passenger(board, x, y):
    if y < 0 or y >= len(board):
        return False
    if x < 0 or x >= len(board[y]):
        return False
    if board[y][x] is None:
        return False
        
    board[y][x] = None
    return True

def get_clicked_cell(mouse_pos, cell_size=100):
    mouse_x, mouse_y = mouse_pos
    
    if not (0 <= mouse_x < 500):
        return None
    if not (0 <= mouse_y < 500):
        return None
        
    x = mouse_x // cell_size
    y = mouse_y // cell_size
    
    return x, y