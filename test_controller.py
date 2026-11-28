from bonus_manager import BonusManager
from achievements import Achievements


board = [
    [1, 2, None, None, None],
    [3, 4, 5, None, None],
    [None, 6, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None]
]

bonus = BonusManager()
achievements = Achievements()

print("BEFORE:")
for row in board:
    print(row)

removed = bonus.use_random(board)
print("\nREMOVED:", removed)
print("BONUSES LEFT:", bonus.charges)

print("\nAFTER:")
for row in board:
    print(row)

awards = achievements.check(
    lines=1,
    score=1000,
    bonuses_used=bonus.used
)

print("\nACHIEVEMENTS:", awards)