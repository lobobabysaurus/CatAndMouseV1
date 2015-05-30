class Renderer:
    """
    Base for other renderers.  Sets up environment info
    """
    def __init__(self, screen):
        """
        Set up width and height and background for class
        :param screen: Surface the game is played on
        """
        self.width, self.height = screen.get_size()
        self.background = screen
