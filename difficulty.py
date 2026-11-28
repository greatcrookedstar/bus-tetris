from settings import (
    START_FALL_DELAY,
    MIN_FALL_DELAY,
    LINES_PER_LEVEL
)

def calculate_level(lines):
    return 1 + lines // LINES_PER_LEVEL

def calculate_speed(level):
    delay = START_FALL_DELAY - (level - 1) * 80
    return max(MIN_FALL_DELAY, delay)

def calculate_points(cleared_lines, level):
    if cleared_lines <= 0:
        return 0

    return 100 * cleared_lines * level