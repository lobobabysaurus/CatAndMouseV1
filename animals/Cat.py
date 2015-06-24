import pygame
from pygame import image, transform

from . import Animal


class Cat(Animal.Animal):
    """
    Cat that will chase mice
    """
    def __init__(self, environment, speed):
        """
        Creates the cat with the proper image
        """
        super().__init__(environment, speed)
        self.wall_modifier = 0
        self.image_name = "media/Cat.png"
        self.root_image = transform.rotate(image.load(self.image_name), 180)
        self.image = self.root_image

    def process_movement(self, input_event):
        """
        Process user input to find out how to move
        :param input_event event Keyboard input provided by the user
        """
        if input_event.type == pygame.KEYUP:
            if input_event.key == pygame.K_UP or input_event.key == pygame.K_DOWN:
                self.y_move = 0
            elif input_event.key == pygame.K_LEFT or input_event.key == pygame.K_RIGHT:
                self.x_move = 0
            self._adjust_bearing()
        elif input_event.type == pygame.KEYDOWN:
            if input_event.key == pygame.K_UP:
                self.y_move = -self.speed
            elif input_event.key == pygame.K_DOWN:
                self.y_move = self.speed
            elif input_event.key == pygame.K_LEFT:
                self.x_move = -self.speed
            elif input_event.key == pygame.K_RIGHT:
                self.x_move = self.speed
            self._adjust_bearing()
