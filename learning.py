import sys
import random
import time

import pygame

pygame.init()

size = width, height = 600, 680
background = pygame.display.set_mode(size)
pygame.display.set_caption("Cat and Mouse")
clock = pygame.time.Clock()
grey = (125, 125, 125)
black = (0, 0, 0)

class Animal(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

all_animals = pygame.sprite.Group()
cat = Animal(black, 30, 10)
cat.rect.x = 0
cat.rect.y = 700
all_animals.add(cat)

mouse_list = pygame.sprite.Group()
for i in range(40):
    mouse = Animal(grey, 10, 10)
    mouse.rect.x = random.randrange(width)
    mouse.rect.y = random.randrange(height)
    mouse_list.add(mouse)
    all_animals.add(mouse)

font = pygame.font.Font(None, 36)
score = 0
score_text = font.render(str(score), 1, (10, 10, 10))
textpos = score_text.get_rect()
textpos.x = width/2

start = time.time()
time_text = font.render(str(start), 1, (10, 10, 10))
time_pos = time_text.get_rect()
time_pos.x = width/2
time_pos.y = height - time_pos.height


while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                cat.rect.x = event.pos[0]
                cat.rect.y = event.pos[1]
                if pygame.sprite.spritecollide(cat, mouse_list, True):
                    score += 1
                    score_text = font.render(str(score), 1, (10, 10, 10))
        if len(mouse_list) > 0:
            time_text = font.render(str(time.time()-start)[:4], 1, (10, 10, 10))

        background.fill((0, 125, 0))
        all_animals.draw(background)
        background.blit(score_text, textpos)
        background.blit(time_text, time_pos)
        pygame.display.flip()
        clock.tick(60)