import random

import pygame

from . import Animal


class Mouse(Animal):
    """
    A Mouse that will scurry around a screen
    """
    def __init__(self, environment, speed):
        """
        Create a mouse
        :param environment: environment the mouse exists in
        :param speed Speed at which the mouse moves
        """
        super().__init__(environment, speed)

    def die(self):
        """
        Causes the mouse to show up as dead
        """
        self.image = pygame.transform.rotate(
            pygame.image.load("media/DeadMouse.png"),
            self.rotation)
        self.is_dead = True

    def flee(self, cat):
        if (cat.rect.x > self.rect.x and self.x_move > 0) or \
                (cat.rect.x < self.rect.x and self.x_move < 0):
            self.x_move = -self.x_move
        if (cat.rect.y > self.rect.y and self.y_move > 0) or \
                (cat.rect.y < self.rect.y and self.y_move < 0):
            self.y_move = -self.y_move

    def move(self):
        """
        Moves the mouse and changes direction if it hits a wall
        """
        super().move()
        if not self.is_dead:
            self._adjust_bearing()
            if self.x_move == 0:
                self.x_move = random.randint(-self.speed, self.speed)
            if self.y_move == 0:
                self.y_move = random.randint(-self.speed, self.speed)
