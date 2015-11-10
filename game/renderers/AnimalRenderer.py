import math
import random

from pygame import sprite

from game.animals import Cat, Mouse
from game.renderers import Renderer


class AnimalRenderer(Renderer):
    """
    Renders and updates animal data uses in the game
    """
    def __init__(self, screen, number_of_mice, flee_zone):
        """
        Setup relevant variables and UI components to draw all of the animals
        :param screen: Surface which the game is played on
        :param number_of_mice: The number of mice involved in the game
        """
        super().__init__(screen)

        self.cat = Cat(self._background, 3)
        self._flee_zone = flee_zone

        self._all_animals = sprite.Group()
        self._all_animals.add(self.cat)
        self._mouse_list = self._create_mouse_pool(number_of_mice)
        self._live_mouse_list = self._mouse_list.copy()
        self._dead_mouse_list = sprite.Group()

    def _create_mouse_pool(self, number_of_mice):
        """
        Create a sprite group of all of the antagonists
        :param number_of_mice: Integer the number of antagonists to create
        :return: a sprite group of all of the mice
        """
        new_mouse_list = sprite.Group()
        for i in range(number_of_mice):
            mouse = Mouse(self._background, random.randint(1, 3))
            new_mouse_list.add(mouse)
            self._all_animals.add(mouse)
        return new_mouse_list

    def detect_close(self):
        """
        Iterates through all live mice and makes them flee if the cat is close
        """
        for mouse in self._live_mouse_list:
            if math.fabs(self.cat.rect.x - mouse.rect.x) < self._flee_zone and\
                   math.fabs(self.cat.rect.y - mouse.rect.y) < self._flee_zone:
                mouse.flee(self.cat)

    def detect_deaths(self, score_and_time):
        """
        Detect mouse deaths, remove them from lists, and update score
        :param score_and_time PlayTextRenderer for the score and time
        :return Number of mice left
        """
        caught_mice = sprite.spritecollide(self.cat, self._mouse_list, False)
        for mouse in caught_mice:
            mouse.die()
            self._mouse_list.remove(mouse)
            self._live_mouse_list.remove(mouse)
            self._dead_mouse_list.add(mouse)
            score_and_time.update_score()
        return len(self._mouse_list)

    def render(self):
        """
        Render the cat and mice
        """
        self._all_animals.update()
        self._all_animals.draw(self._background)
        self._background.blit(self.cat.image, self.cat.rect)
