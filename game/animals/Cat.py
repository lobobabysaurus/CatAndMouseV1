import pygame
from pygame import image, transform

from game.animals import Animal


class Cat(Animal):
    """
    Cat that will chase mice
    """
    def __init__(self, environment, _speed):
        """
        Creates the cat with the proper image
        """
        super().__init__(environment, _speed)

        self._wall_modifier = 0
        image_name = "media/Cat.png"
        self._root_image = transform.rotate(image.load(image_name), 180)
        self.image = self._root_image

    def process_movement(self, input_event):
        """
        Process user input to find out how to move
        :param input_event event Keyboard input provided by the user
        """
        if input_event.type == pygame.KEYUP:
            self._handle_key_up(input_event)
        elif input_event.type == pygame.KEYDOWN:
            self._handle_key_down(input_event)

    def _handle_key_down(self, input_event):
        """
        Handle what happense when the user presses down a key
        :param input_event Key press
        """
        if input_event.key == pygame.K_UP:
            self._y_move = -self._speed
        elif input_event.key == pygame.K_DOWN:
            self._y_move = self._speed
        elif input_event.key == pygame.K_LEFT:
            self._x_move = -self._speed
        elif input_event.key == pygame.K_RIGHT:
            self._x_move = self._speed
        self._adjust_bearing()

    def _handle_key_up(self, input_event):
        """
        Handle what happense when the user releases a key
        :param input_event Key press
        """
        if input_event.key == pygame.K_UP or \
                input_event.key == pygame.K_DOWN:
            self._y_move = 0
        elif input_event.key == pygame.K_LEFT or \
                input_event.key == pygame.K_RIGHT:
            self._x_move = 0
        self._adjust_bearing()
