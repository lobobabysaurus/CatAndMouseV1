from pygame.font import Font

from . import Renderer


class TextRenderer(Renderer):
    """
    Base for renderers of text
    """
    def __init__(self, screen):
        """
        Sets up font display based info
        :param screen: Surface the game is played on
        """
        super().__init__(screen)
        self.text_color = (10, 10, 10)
        self.font_size = 36
        self.font_type = None
        self.font = Font(self.font_type, self.font_size)
