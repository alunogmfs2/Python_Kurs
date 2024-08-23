import pgzrun
import random

WIDTH = 400
HEIGHT = 708

bird = Actor('bird1', (75, 200))
pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))

pipe_gap_y = random.randint(200, HEIGHT - 200)
pipe_top.pos = (WIDTH, pipe_gap_y - 130 // 2)
pipe_bottom.pos = (WIDTH, pipe_gap_y + 130 // 2)

bird.dead = False
bird.vy = 0

bird.points = 0

FLAP_VELOCITY = -6.5

def draw():
    screen.blit('background', (0, 0))
    bird.draw()
    pipe_top.draw()
    pipe_bottom.draw()
    screen.draw.text(str(bird.points), topright=(WIDTH - 40, 10))

def update():
    screen.blit('background', (0, 0))
    bird.draw()
    pipe_top.draw()
    pipe_bottom.draw()
    update_pipes()
    update_bird()

def reset_pipe():
    global pipe_gap_y, pipe_top, pipe_bottom
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - 130 // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + 130 // 2)

def update_pipes():
    pipe_top.left -= 3
    pipe_bottom.left -= 3
    if pipe_top.right < 0:
        reset_pipe()

def update_bird():
    uy = bird.vy
    bird.vy += 0.3
    bird.y += bird.vy
    bird.x = 75

    if not bird.dead:
        if bird.vy < -3:
            bird.image = 'bird2'
        else:
            bird.image = 'bird1'

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'birddead'
        bird.points = 0

    if bird.x == pipe_top.x or bird.x == pipe_top.x + 1 or bird.x == pipe_top.x - 1 and not bird.dead:
        bird.points += 1

    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.vy = 0
        reset_pipe()

def on_key_down():
    if not bird.dead:
        bird.vy = FLAP_VELOCITY

pgzrun.go()
