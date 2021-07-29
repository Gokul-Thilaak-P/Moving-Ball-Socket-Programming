import socket
import pygame
import pickle


pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("move_the_ball")
run = True

SERVER = "192.168.29.71"
PORT = 9999
ADDRESS = (SERVER, PORT)

player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
player.connect(ADDRESS)


p1 = pickle.loads(player.recv(2048))

while run:
    pygame.time.delay(50)

    player.send(pickle.dumps(p1))

    p2 = pickle.loads(player.recv(2048))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_RIGHT]:
        if p1.centre_x < 500:
            p1.centre_x += p1.velocity
        else:
            p1.centre_x = 0

    if keys[pygame.K_LEFT]:
        if p1.centre_x > 0:
            p1.centre_x -= p1.velocity
        else:
            p1.centre_x = 500

    if not p1.isjumping:
        if keys[pygame.K_UP]:
            if p1.centre_y > 0:
                p1.centre_y -= p1.velocity
            else:
                p1.centre_y = 500

        if keys[pygame.K_DOWN]:
            if p1.centre_y < 500:
                p1.centre_y += p1.velocity
            else:
                p1.centre_y = 0

        if keys[pygame.K_SPACE]:
            p1.isjumping = True

    if p1.isjumping:
        if p1.jump_pos >= -10:
            neg = 1
            if p1.jump_pos < 0:
                neg = -1
            p1.centre_y -= (p1.jump_pos ** 2) // 2 * neg
            p1.jump_pos -= 2
        else:
            p1.jump_pos = 10
            p1.isjumping = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, p1.color, (p1.centre_x, p1.centre_y), p1.radius)
    pygame.draw.circle(screen, p2.color, (p2.centre_x, p2.centre_y), p2.radius)
    pygame.display.update()
pygame.quit()
