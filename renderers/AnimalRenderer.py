import math
import random

from pygame import sprite

from animals import Cat, Mouse
from . import Renderer


class AnimalRenderer(Renderer):
    """
    Renders and updates animal data uses in the game
    """
    def __init__(self, screen, number_of_mice, flee_zone):
        """
        Setup relevant class variables and UI components to draw all of the game animals
        :param screen: Surface which the game is played on
        :param number_of_mice: The number of mice involved in the game
        """
        super().__init__(screen)

        self.all_animals = sprite.Group()
        # Create the protagonist
        self.cat = Cat(self.background, 3)
        self.all_animals.add(self.cat)

        self.total_mice = number_of_mice

        self.mouse_list = self._create_mouse_pool(self.total_mice)
        self.live_mouse_list = self.mouse_list.copy()
        self.dead_mouse_list = sprite.Group()

        self.flee_zone = flee_zone

    def _create_mouse_pool(self, number_of_mice):
        """
        Create a sprite group of all of the antagonists
        :param number_of_mice: Integer the number of antagonists to create
        :return: a sprite group of all of the mice
        """
        new_mouse_list = sprite.Group()
        for i in range(number_of_mice):
            mouse = Mouse(self.background, random.randint(1, 3))
            new_mouse_list.add(mouse)
            self.all_animals.add(mouse)
        return new_mouse_list

    def detect_close(self):
        """
        Iterates through all live mice and makes them flee if the cat is close
        """
        for mouse in self.live_mouse_list:
            if math.fabs(self.cat.rect.x - mouse.rect.x) < self.flee_zone and \
                    math.fabs(self.cat.rect.y - mouse.rect.y) < self.flee_zone:
                mouse.flee(self.cat)

    def detect_deaths(self, score_and_time):
        """
        Find out if any mice have been killed, let them die, remove them from detection lists, and update score
        :param score_and_time Play Text Renderer for the score and time
        :return Number of mice left
        """
        caught_mice = sprite.spritecollide(self.cat, self.mouse_list, False)
        for mouse in caught_mice:
            mouse.die()
            self.mouse_list.remove(mouse)
            self.live_mouse_list.remove(mouse)
            self.dead_mouse_list.add(mouse)
            score_and_time.update_score()
        return len(self.mouse_list)
            
    def render(self):
        """
        Render the cat and mice
        """
        self.all_animals.update()
        self.all_animals.draw(self.background)
        self.background.blit(self.cat.image, self.cat.rect)
