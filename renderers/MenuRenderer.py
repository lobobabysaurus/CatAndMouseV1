import sys

from pygame import K_UP, K_DOWN, K_RETURN, mixer

from renderers import TextRenderer


class MenuRenderer(TextRenderer):
    """
    Render menu options
    """
    def __init__(self, screen, option_texts):
        """
        Setup class variables and containers for text
        :param screen: Surface where the menu is rendered
        :param option_texts: List of all option texts
        """
        super().__init__(screen)

        self.menu_shown = True
        self._active_color = (0, 158, 138)
        self._active_index = 0
        self._menu_options = self._create_options(option_texts)
        self._meow = mixer.Sound('media/meow.ogg')
        self._texts = option_texts

    def _create_options(self, option_list):
        """
        Create a menu option
        :param option_list A list of text for options that should be created
        :return Dictionary mapping option surfaces to relevant rectangles
        """
        half = len(option_list)/2
        options = {}
        for index, option in enumerate(option_list):
            if self._active_index == index:
                option_text = self._font.render(option, 1, self._active_color)
            else:
                option_text = self._font.render(option, 1, self._text_color)
            option_rect = option_text.get_rect()
            option_rect.x = self._width/2 - option_rect.width/2
            option_rect.y = self._height/2 - option_rect.height/2
            if index < half:
                option_rect.y -= (self._font_size * (half-index))
            else:
                option_rect.y += (self._font_size * (index-half))
            options[option_text] = {
                "text": option, 'rect': option_rect, 'order': index}
        return options

    def handle_key_press(self, user_input):
        """
        Handle key presses to navigate the menu
        :param user_input Keyboard event by the user
        """
        if user_input.key == K_UP:
            self._move_up()
        elif user_input.key == K_DOWN:
            self._move_down()
        elif user_input.key == K_RETURN:
            if self._active_index == 0:
                self._meow.play()
                return True
            elif self._active_index == 1:
                self.menu_shown = False
            elif self._active_index == 3:
                sys.exit()

    def handle_return(self, user_input):
        """
        Handle returning from a sub-menu
        :param user_input Keyboard event by the user
        """
        if user_input.key == K_RETURN:
            self.menu_shown = True

    def render(self):
        """
        Render menu options
        """
        for option in self._menu_options:
            self._background.blit(option, self._menu_options[option]['rect'])

    def _move_up(self):
        """
        Rerender menu with the active item now above the previously active item
        """
        if self._active_index != 0:
            self._active_index -= 1
            self._menu_options = self._create_options(self._texts)

    def _move_down(self):
        """
        Rerender menu the active item now below the previously active item
        """
        if self._active_index != len(self._texts)-1:
            self._active_index += 1
            self._menu_options = self._create_options(self._texts)
