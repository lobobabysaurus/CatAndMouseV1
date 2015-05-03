import random

import pygame

from animals import Animal


class Mouse(Animal.Animal):
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

    def die(self):
        """
        Causes the mouse to show up as dead
        """
        self.image = pygame.transform.rotate(
            pygame.image.load("media/DeadMouse.png"),
            self.rotation)
        self.is_dead = True