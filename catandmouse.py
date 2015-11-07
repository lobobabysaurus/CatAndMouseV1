import sys

import pygame

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
        pygame.mixer.init()
        self._clock = pygame.time.Clock()

        pygame.display.set_caption("Cat and Mouse")
        size = width, height = 600, 680
        self._background = pygame.display.set_mode(size)
        self._tile = self._get_floor(size)

        menu_options = ["Start", "Instructions", "Options", "Quit", ]
        self._menu = MenuRenderer(self._background, menu_options)

        self._mouse_number = 10
        self._flee_zone = 75
        self._score_and_time = PlayTextRenderer(
            self._background, self._mouse_number)
        self._animals = AnimalRenderer(
            self._background, self._mouse_number, self._flee_zone)

    def present_menu(self, rerun=False):
        """
        Present the game selection menu to the user
        :param rerun: Determine if it the first run or a rerun of the game
        """
        started = False
        render_list = [self._animals.render, self._menu.render]
        if rerun:
            render_list.append(self._score_and_time.render)
        while not started:
            # Handle user input
            for user_input in pygame.event.get():
                if user_input.type == pygame.QUIT:
                    sys.exit()
                elif user_input.type == pygame.KEYDOWN:
                    if self._menu.menu_shown is True:
                        started = self._menu.handle_key_press(user_input)
                    else:
                        self._menu.handle_return(user_input)
            self._render_and_draw(render_list)

    def reset_game(self):
        """
        Reset the game play screen
        """
        self._animals = AnimalRenderer(
            self._background, self._mouse_number, self._flee_zone)
        self._score_and_time = PlayTextRenderer(
            self._background, self._mouse_number)

    def play_game(self):
        """
        Main game loop
        """
        all_caught = False
        render_list = [self._animals.render, self._score_and_time.render]
        while not all_caught:
            # Handle user input
            for user_input in pygame.event.get():
                if user_input.type == pygame.QUIT:
                    sys.exit()
                elif user_input.type == pygame.KEYUP or \
                        user_input.type == pygame.KEYDOWN:
                    self._animals.cat.process_movement(user_input)
            if self._animals.detect_deaths(self._score_and_time) == 0:
                all_caught = True
            self._animals.detect_close()
            self._render_and_draw(render_list)

    @staticmethod
    def _get_floor(background_size):
        """
        Given the size of the background, draw a floor that is covered by tiles
        :param background_size: Size of the background
        :return: Surface object covered in flooring
        """
        tile = pygame.Surface(background_size)
        tile_image = pygame.image.load('media/TileFloor.png')
        tile_size = tile_image.get_size()
        tile_rect = tile_image.get_rect()
        for y in range(0, background_size[1], tile_size[1]):
            for x in range(0, background_size[0], tile_size[0]):
                tile_rect.x = x
                tile_rect.y = y
                tile.blit(tile_image, tile_rect)
        return tile

    def _render_and_draw(self, render_array):
        """
        Clear screen, render all relevant components, then redraw the screen
        :param render_array: Array of render methods to call
        """
        self._background.blit(self._tile, self._tile.get_rect())
        for render in render_array:
            render()
        pygame.display.flip()
        self._clock.tick(60)
