class Renderer:
    """
    Base for other renderers.  Sets up environment info
    """
    def __init__(self, screen):
        """
        Set up width and height and background for class
        :param screen: Surface the game is played on
        """
        self._width, self._height = screen.get_size()
        self._background = screen
