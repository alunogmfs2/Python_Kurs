import pgzrun

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.fill((255, 203, 219))
    alien.draw()

pgzrun.go()
