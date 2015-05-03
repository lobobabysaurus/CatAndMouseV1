import sys
import random
import time

import pygame

from animals import Mouse
from animals import Cat


class CatAndMouseGame:
    """
    A game where the great cat Lobo kills the evil mouse
    """
    def __init__(self):
        """
        Setup the environment and participants for a game of cat and mouse
        """
        pygame.init()

        size = self.width, self.height = 600, 680
        self.background = pygame.display.set_mode(size)
        pygame.display.set_caption("Cat and Mouse")

        self.clock = pygame.time.Clock()

        self.all_animals = pygame.sprite.Group()

        # Create the protagonist
        self.cat = Cat.Cat(self.background, 3)
        self.all_animals.add(self.cat)

        # Create the antagonists
        self.total_mice = 10
        self.mouse_list = self._create_mouse_pool(self.total_mice)
        self.dead_mouse_list = pygame.sprite.Group()

        # Set the score display
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.score_text = self.font.render(str(self.score), 1, (10, 10, 10))
        self.score_pos = self.score_text.get_rect()
        self.score_pos.x = self.width/2

        # Set the time display
        self.start = time.time()
        self.end = self.start +(self.total_mice*2.5)
        self.time_text = self.font.render(str(self.start), 1, (10, 10, 10))
        self.time_pos = self.time_text.get_rect()
        self.time_pos.x = self.width/2
        self.time_pos.y = self.height - self.time_pos.height

    def _create_mouse_pool(self, number_of_mice):
        """
        Create a sprite group of all of the antagonists
        :param number_of_mice: Integer the number of antagonists to create
        :return: a sprite group of all of the mice
        """
        new_mouse_list = pygame.sprite.Group()
        for i in range(number_of_mice):
            mouse = Mouse.Mouse(self.background, random.randint(1, 3))
            new_mouse_list.add(mouse)
            self.all_animals.add(mouse)
        return new_mouse_list

    def play_game(self):
        """
        Main game loop
        """
        all_caught = False
        while not all_caught:
            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                    self.cat.process_movement(event)

            self.detect_deaths()
            self.draw_screen()

    def detect_deaths(self):
        """
        Find out if any mice have been killed, let them die, remove them from detection lists, and update score
        """
        caught_mice = pygame.sprite.spritecollide(self.cat, self.mouse_list, False)
        for mouse in caught_mice:
            mouse.die()
            self.mouse_list.remove(mouse)
            self.dead_mouse_list.add(mouse)
            self.score += 1
            self.score_text = self.font.render(str(self.score), 1, (10, 10, 10))

    def draw_screen(self):
        """
        Draws all objects to the screen and update the timer
        """
        if len(self.mouse_list) > 0:
            self.time_text = self.font.render(str(self.end-time.time())[:4], 1, (10, 10, 10))
        self.background.fill((0, 125, 0))
        self.all_animals.update()
        self.all_animals.draw(self.background)
        self.background.blit(self.cat.image, self.cat.rect)
        self.background.blit(self.score_text, self.score_pos)
        self.background.blit(self.time_text, self.time_pos)
        pygame.display.flip()
        self.clock.tick(60)

cmg = CatAndMouseGame()
cmg.play_game()
