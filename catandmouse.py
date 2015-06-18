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
        menu_options = ["Start", "Instructions", "Options", "Quit", ]
        self.menu = MenuRenderer(self.background, menu_options)
        self.score_and_time = PlayTextRenderer(self.background, self.mouse_number)
        self.animals = AnimalRenderer(self.background, self.mouse_number)

    def present_menu(self, rerun=False):
        """
        Show a menu to the user
        """
        started = False
        render_list = [self.animals.render, self.menu.render]
        if rerun:
            render_list.append(self.score_and_time.render)
        while not started:
            # Handle user input
            for user_input in event.get():
                if user_input.type == pygame.QUIT:
                    sys.exit()
                elif user_input.type == pygame.KEYDOWN:
                    if self.menu.menu_shown is True:
                        started = self.menu.handle_key_press(user_input)
                    else:
                        self.menu.handle_return(user_input)
            self.render_and_draw(render_list)

    def reset_game(self):
        """
        Reset the game play screen
        """
        self.animals = AnimalRenderer(self.background, self.mouse_number)
        self.score_and_time = PlayTextRenderer(self.background, self.mouse_number)

    def play_game(self):
        """
        Main game loop
        """
        all_caught = False
        render_list = [self.animals.render, self.score_and_time.render]
        while not all_caught:
            # Handle user input
            for user_input in event.get():
                if user_input.type == pygame.QUIT:
                    sys.exit()
                elif user_input.type == pygame.KEYUP or user_input.type == pygame.KEYDOWN:
                    self.animals.cat.process_movement(user_input)
            if self.animals.detect_deaths(self.score_and_time) == 0:
                all_caught = True
            self.render_and_draw(render_list)

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
first_run = True
while True:
    cmg.present_menu(not first_run)
    cmg.reset_game()
    cmg.play_game()
    first_run = False
