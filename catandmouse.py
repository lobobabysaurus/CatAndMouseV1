import sys
import random
import time

import pygame

import animals


class CatAndMouseGame:
    def __init__(self):
        pygame.init()

        size = self.width, self.height = 600, 680
        self.background = pygame.display.set_mode(size)
        pygame.display.set_caption("Cat and Mouse")
        self.clock = pygame.time.Clock()

        self.all_animals = pygame.sprite.Group()

        #Create the protagonist
        self.cat = animals.Cat()
        self.cat.rect.x = random.randrange(self.width)
        self.cat.rect.y = random.randrange(self.height)
        self.all_animals.add(self.cat)

        #Create the antagonists
        self.mouse_list = self.__create_mouse_pool()
        self.dead_mouse_list = pygame.sprite.Group()

        #Set the score display
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.score_text = self.font.render(str(self.score), 1, (10, 10, 10))
        self.textpos = self.score_text.get_rect()
        self.textpos.x = self.width/2

        #Set the time display
        self.start = time.time()
        self.time_text = self.font.render(str(self.start), 1, (10, 10, 10))
        self.time_pos = self.time_text.get_rect()
        self.time_pos.x = self.width/2
        self.time_pos.y = self.height - self.time_pos.height

    def __create_mouse_pool(self):
        """

        :return:
        """
        list = pygame.sprite.Group()
        for i in range(10):
            mouse = animals.Mouse(self.background)
            mouse.rect.x = random.randrange(self.width)
            mouse.rect.y = random.randrange(self.height)
            list.add(mouse)
            self.all_animals.add(mouse)
        return list

    def play_game(self):
        """
        Main game loop
        :return:
        """
        all_caught = False;
        while not all_caught:
            #Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.cat.rect.x = event.pos[0]-10
                    self.cat.rect.y = event.pos[1]-15

            #Detect if any mice have been caught
            caught_mice = pygame.sprite.spritecollide(self.cat, self.mouse_list, False)
            for mouse in caught_mice:
                mouse.die()
                self.mouse_list.remove(mouse)
                self.dead_mouse_list.add(mouse)
                self.score += 1
                self.score_text = self.font.render(str(self.score), 1, (10, 10, 10))

            #If any mice are left update the time and move the still alive guys otherwise end the game
            if len(self.mouse_list) > 0:
                self.time_text = self.font.render(str(time.time()-self.start)[:4], 1, (10, 10, 10))
                for mouse in self.mouse_list:
                    mouse.move()
            # else:
            #    all_caught = True

            #Draw all of the required data
            self.background.fill((0, 125, 0))
            self.all_animals.draw(self.background)
            self.background.blit(self.score_text, self.textpos)
            self.background.blit(self.time_text, self.time_pos)
            pygame.display.flip()
            self.clock.tick(60)

cmg = CatAndMouseGame()
cmg.play_game()
