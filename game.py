import pygame
import random
from controls import handle_controls
from sound_mamnger import SoundManager
from records import load_record,save_record
from difficulty import(calculate_level,calculate_speed,calculate_points)
pygame.init()
sounds =  SoundManager()
sound.load_sound("move",'movie.wav')
sound.load_sound("rotate",'rotate.wav')
sound.load_sound("land",'land.wav')
sound.load_sound("clear",'clear.wav')
sound.play_music()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bus Tetris")
clock = pygame.time.Clock()
backgound, characters =  load_assets()
game =  Game()
state =  "menu"
paused =  False
selecting =  False
running  =  True
fall_timer  =  0
while running:
    dt  =  clock.tick(60)

    if state == "playing" and not paused:
        fall_timer += dt
    if state == "menu":
        start_button, quit_button =  draw_menu(screen)
    else:
        random_button,select_button=  draw_game(screen,game,background,characters,paused,selecting)
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running  = False
        
        if event.type  == pygame.MOUSEBUTTONDOWN:
             if event.button != 1:
                    continue
                mx, my = event.pos
                
                if state == "menu":
                    if start_button.collidepoint(mx, my):
                        game.reset()
                        state = "playing"
                        paused = False
                        selecting = False
                        fall_timer = 0
                    elif quit_button.collidepoint(mx, my):
                        running = False
                        
                elif state == "playing" and not paused:
                    if select_button.collidepoint(mx, my):
                        if not game.game_over:
                            selecting = not selecting
                    elif random_button.collidepoint(mx, my):
                        if not game.game_over:
                            remove_random(game)
                            selecting = False
                    elif selecting and not game.game_over:
                        x = (mx - BOARD_X) // CELL
                        y = (my - BOARD_Y) // CELL
                        
                        if 0 <= x < 5 and 0 <= y < 5:
                            if remove_selected(game, x, y):
                                selecting = False

            # Обработка клавиатуры
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if state == "playing" and selecting:
                        selecting = False
                    elif state == "playing":
                        state = "menu"
                        paused = False

        # Логика падения фигур (таймер)
        if state == "playing" and not paused:
            fall_timer += dt
            # Допустим, задержка падения 500 мс (0.5 сек)
            if fall_timer >= 500 and not game.game_over: 
                game.move(0, 1)
                fall_timer = 0

        # Обновление экрана (эта строка была обрезана, но она обязательна)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


SHAPES = [[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (0, 1), (1, 1)],[(0, 0), (1, 0), (2, 0), (1, 1)],[(0, 0), (0, 1), (0, 2), (1, 2)],[(1, 0), (1, 1), (1, 2), (0, 2)],[(0, 0), (1, 0), (1, 1), (2, 1)],[(1, 0), (2, 0), (0, 1), (1, 1)]]
board = [[None] * COLS for _ in range(ROWS)]
score = 0
lines = 0
level = 1
# Загружаем изображения
background = pygame.image.load("assets/bus_background.jpg")
background = pygame.transform.scale(background, (500, 500))
pygame.mixer.music.load("assets/sounds/bus_background.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
people = []
for i in range(1,14):
    image= (pygame.image.load(f"assets/p1.png"),pygame.image.load(f"assets/p2.png"),pygame.image.load(f"assets/p3.png"))
    people.append(pygame.transform.scale(image,(CELL,CELL)))
def new_piece():
    shape  =   random.choice(SHAPES)
    width  =  max(x for x,y in shape)+1
    return  {
        "shape":shape[:]
        "x":(COLS-widht)//2
        "y":0
        "people":random.sample(range(13),4)
    }
def get_cells(piecel,dx= 0 , dy = 0, shape  = None):
    shape   =  shape if shape is not None else piece["shape"]
    return [
        (piece["x"]+x+dx,piece["y"]+y+dy)
        for x,y in shape
    ]
def valid(piece,dx= 0,dy  = 0 ,shape  =  None):
    for x,y in get_cells(piece,dx,dy, shape =  None):
        if x<0 or x>=COLS or y>=ROWS:
            return False
        if y>=0 and board[y][x] is not None:
            return False
    return True
def rotate(piece):
    if piece["shape"]==SHAPES[1]:
        return 
    rotated =  [(-y,x) for x,y in piece["shape"]]

    min_x  =  min(x for x,y in rotated)
    min_y  =  min(y for x,y in rotated)

    rotated = [
        (x-min_x,y-min_y)
        for x,y in rotated
    ]
    if valid (piece,shape  =  rotated):
        piece["shape"]=  rotated

def clean_lines():
    global board, score, lines, level

    remaining  =   [
        row for row in board
        if not all(cell is not None for cell in row)
    ]

    removed =  ROWS  - len(remaining)

    if removed:
        board = [[None]*COLS for _ in range(removed)]+remaining
        lines +=removed *100
        level = 1+lines //5

def lock_piece(piece):
    for index,(x,y) in enumerate(get_cells(piece)):
        if 0<=y< ROWS:
            board[y][x]= piece["people"][index]
    clear_lines()
def draw(piece):
    screen.fill((233, 223, 209))
    screen.blit(background, (0, 0))

    # Уже упавшие пассажиры
    for y in range(ROWS):
        for x in range(COLS):
            person_id = board[y][x]

            if person_id is not None:
                screen.blit(
                    people[person_id],
                    (x * CELL, y * CELL)
                )

    # Падающая фигура
    if piece is not None:
        for index, (x, y) in enumerate(get_cells(piece)):
            if 0 <= y < ROWS:
                screen.blit(
                    people[piece["people"][index]],
                    (x * CELL, y * CELL)
                )

    # Линии сетки
    for i in range(COLS + 1):
        pygame.draw.line(
            screen, (120, 100, 120),
            (i * CELL, 0), (i * CELL, 500), 1
        )

    for i in range(ROWS + 1):
        pygame.draw.line(
            screen, (120, 100, 120),
            (0, i * CELL), (500, i * CELL), 1
        )

    # Временная панель счёта
    font = pygame.font.SysFont("arial", 28, bold=True)

    stats = [
        f"SCORE: {score}",
        f"LEVEL: {level}",
        f"LINES: {lines}"
    ]

    for i, text in enumerate(stats):
        label = font.render(text, True, (98, 81, 93))
        screen.blit(label, (520, 70 + i * 65))

    pygame.display.flip()

piece = new_piece()
fall_timer = 0
running = True

while running:
    dt = clock.tick(60)
    fall_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and valid(piece, dx=-1):
                piece["x"] -= 1

            elif event.key == pygame.K_RIGHT and valid(piece, dx=1):
                piece["x"] += 1

            elif event.key == pygame.K_DOWN and valid(piece, dy=1):
                piece["y"] += 1

            elif event.key == pygame.K_UP:
                rotate(piece)

    fall_delay = max(150, 800 - (level - 1) * 80)

    if fall_timer >= fall_delay:
        fall_timer = 0

        if valid(piece, dy=1):
            piece["y"] += 1
        else:
            lock_piece(piece)
            piece = new_piece()

            if not valid(piece):
                print("GAME OVER")
                print("SCORE:", score)
                running = False

    draw(piece)

pygame.quit()
