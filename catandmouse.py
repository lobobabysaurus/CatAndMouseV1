import sys

import pygame
from pygame import display, time, event

from renderers.AnimalRenderer import AnimalRenderer
from renderers.PlayTextRenderer import PlayTextRenderer
from renderers.MenuRenderer import MenuRenderer


class CatAndMouseGame:
    """
    A game where the great cat Lobo kills the evil mouse
    """
    def __init__(self):
        """
        Setup the environment and participants for a game of cat and mouse
        """
        pygame.init()
        self.mouse_number = 10
        size = self.width, self.height = 600, 680
        self.background = display.set_mode(size)
        self.background_color = (75, 156, 212)
        display.set_caption("Cat and Mouse")

        self.clock = time.Clock()
        self.menu = MenuRenderer(self.background, ("Start", "Options", ))
        self.score_and_time = PlayTextRenderer(self.background, self.mouse_number)
        self.animals = AnimalRenderer(self.background, self.mouse_number)

    def present_menu(self):
        """
        Show a menu to the user
        """
        started = False
        while not started:
            # Handle user input
            for user_input in event.get():
                if user_input.type == pygame.QUIT:
                    sys.exit()
                elif user_input.type == pygame.MOUSEBUTTONDOWN and user_input.button == 1:
                        pos = pygame.mouse.get_pos()
                        for option in self.menu.menu_options:
                            if self.menu.menu_options[option].collidepoint(pos):
                                started = True
            self.render_and_draw((self.animals.render, self.menu.render))

    def play_game(self):
        """
        Main game loop
        """
        all_caught = False
        while not all_caught:
            # Handle user input
            for user_input in event.get():
                if user_input.type == pygame.QUIT:
                    sys.exit()
                elif user_input.type == pygame.KEYUP or user_input.type == pygame.KEYDOWN:
                    self.animals.cat.process_movement(user_input)
            self.animals.detect_deaths(self.score_and_time)
            self.render_and_draw((self.animals.render, self.score_and_time.render))

    def render_and_draw(self, render_array):
        """
        Clear the screen, render all relevant components, and then redraw the screen
        :param render_array: Array of render methods to be called within the method
        """
        self.background.fill(self.background_color)
        for render in render_array:
            render()
        display.flip()
        self.clock.tick(60)

cmg = CatAndMouseGame()
cmg.present_menu()
cmg.play_game()
