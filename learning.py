import sys

import pygame

pygame.init()

size = width, height = 640, 680
speed = [1, 1]

background = pygame.display.set_mode(size)
snake = pygame.image.load("media/pypy-logo.png")
snakerect = snake.get_rect()

snakerect.x = 0
snakerect.y = 700

drop = pygame.image.load("media/water-droplet.png")
dropRect = drop.get_rect()

dropRect.x = 400
dropRect.y = 0

font = pygame.font.Font(None, 36)
score = 0
score_text = font.render(str(score), 1, (10, 10, 10))
textpos = score_text.get_rect()
textpos.x = background.get_width()/2;

while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                snakerect.x = event.pos[0]
                snakerect.y = event.pos[1]
                if snakerect.colliderect(dropRect):
                    score += 1
                    score_text = font.render(str(score), 1, (10, 10, 10))

        dropRect.move_ip(0, 1)
        background.fill((255, 125, 255))
        background.blit(score_text, textpos)
        background.blit(snake, snakerect)
        background.blit(drop, dropRect)
        pygame.display.flip()