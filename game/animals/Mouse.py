import random

import pygame

from . import Animal


class Mouse(Animal):
    """
    A Mouse that will scurry around a screen
    """
    def __init__(self, environment, _speed):
        """
        Create a mouse
        :param environment: environment the mouse exists in
        :param _speed _speed at which the mouse moves
        """
        super().__init__(environment, _speed)

    def die(self):
        """
        Causes the mouse to show up as dead
        """
        self.image = pygame.transform.rotate(
            pygame.image.load("media/DeadMouse.png"),
            self._rotation)
        self.is_dead = True

    def flee(self, cat):
        """
        Have the mouse flee from the cat
        :param cat user controlled cat
        """
        if (cat.rect.x > self.rect.x and self._x_move > 0) or \
                (cat.rect.x < self.rect.x and self._x_move < 0):
            self._x_move = -self._x_move
        if (cat.rect.y > self.rect.y and self._y_move > 0) or \
                (cat.rect.y < self.rect.y and self._y_move < 0):
            self._y_move = -self._y_move

    def move(self):
        """
        Moves the mouse and changes direction if it hits a wall
        """
        super().move()
        if not self.is_dead:
            self._adjust_bearing()
            if self._x_move == 0:
                self._x_move = random.randint(-self._speed, self._speed)
            if self._y_move == 0:
                self._y_move = random.randint(-self._speed, self._speed)
