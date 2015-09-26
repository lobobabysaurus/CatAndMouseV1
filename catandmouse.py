import sys

import pygame
from pygame import display, Surface, time, event

from renderers import AnimalRenderer, PlayTextRenderer, MenuRenderer


class CatAndMouseGame:
    """
    A game where the great cat Lobo kills the evil mice
    """
    def __init__(self):
        """
        Setup the environment and participants for a game of cat and mouse
        """
        pygame.init()
        self.mouse_number = 10
        self.flee_zone = 75
        size = self.width, self.height = 600, 680
        self.background = display.set_mode(size)
        self.tile = self.get_floor(size)
        display.set_caption("Cat and Mouse")

        self.clock = time.Clock()
        menu_options = ["Start", "Instructions", "Options", "Quit", ]
        self.menu = MenuRenderer(self.background, menu_options)
        self.score_and_time = PlayTextRenderer(self.background, self.mouse_number)
        self.animals = AnimalRenderer(self.background, self.mouse_number, self.flee_zone)

    @staticmethod
    def get_floor(background_size):
        """
        Given the size of the background, draw a floor that is covered by tiles to match the floor
        :param background_size: Size of the background
        :return: Surface object covered in flooring
        """
        tile = Surface(background_size)
        tile_image = pygame.image.load('media/TileFloor.png')
        tile_size = tile_image.get_size()
        tile_rect = tile_image.get_rect()
        for y in range(0, background_size[1], tile_size[1]):
            for x in range(0, background_size[0], tile_size[0]):
                tile_rect.x = x
                tile_rect.y = y
                tile.blit(tile_image, tile_rect)
        return tile

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
        self.animals = AnimalRenderer(self.background, self.mouse_number, self.flee_zone)
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
            self.animals.detect_close()
            self.render_and_draw(render_list)

    def render_and_draw(self, render_array):
        """
        Clear the screen, render all relevant components, and then redraw the screen
        :param render_array: Array of render methods to be called within the method
        """
        self.background.blit(self.tile, self.tile.get_rect())
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
