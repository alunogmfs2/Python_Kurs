import pgzrun

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

alien.topright = 0, 10

cont = 0

def draw():
    screen.fill((255, 203, 219))
    alien.draw()

def update():
    alien.left = alien.left + 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    global cont
    if alien.collidepoint(pos):
        cont += 1
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.2)


def set_alien_normal():
    alien.image = 'alien'
    print('Looser!')

pgzrun.go()

print(cont)
