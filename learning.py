import sys, pygame
pygame.init()

size = width, height = 640, 680
speed = [1, 1]

screen = pygame.display.set_mode(size)
ball = pygame.image.load("pypy-logo.png")
ballrect = ball.get_rect()

while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                ballrect.x = event.pos[0]
                ballrect.y = event.pos[1]
                screen.fill((255, 125, 255))
                screen.blit(ball, ballrect)
                pygame.display.flip()