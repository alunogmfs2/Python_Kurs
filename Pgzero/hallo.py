import pgzrun

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
        sounds.eep.play()
        alien.image = 'alien_hurt'
        print('Ouch!')
    else:
        alien.image = 'alien'
        print('Looser!')

pgzrun.go()
