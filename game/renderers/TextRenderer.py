from pygame.font import Font

from game.renderers import Renderer


class TextRenderer(Renderer):
    """
    Base for renderers of text
    """
    def __init__(self, screen):
        """
        Sets up _font display based info
        :param screen: Surface the game is played on
        """
        super().__init__(screen)

        self._font_size = 36
        self._font_type = None
        self._font = Font(self._font_type, self._font_size)
        self._text_color = (10, 10, 10)
