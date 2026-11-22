from controller import (
    remove_random_passengers,
    remove_selected_passenger
)


class BonusManager:
    def __init__(self):
        self.charges = 1
        self.used = 0

    def add_bonus(self):
        self.charges += 1

    def use_random(self, board):
        if self.charges <= 0:
            return 0
        
        removed = remove_random_passengers(board)
        
        if removed > 0:
            self.charges -= 1
            self.used += 1
        return removed

    def use_selected(self, board, x, y):
        if self.charges <= 0:
            return False
        
        success = remove_selected_passenger(
            board, x, y
        )
        
        if success:
            self.charges -= 1
            self.used += 1
            
        return success