import pgzrun
import time

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

alien.topright = 0, 10

def draw():
    screen.fill((255, 203, 219))
    alien.draw()

def update():
    alien.left = alien.left + 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.2)


def set_alien_normal():
    alien.image = 'alien'
    print('Looser!')

pgzrun.go()
