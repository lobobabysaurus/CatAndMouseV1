from renderers.TextRenderer import TextRenderer


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
        self.menu_options = self.create_options(option_texts)

    def create_options(self, option_list):
        """
        Create a menu option
        :param option_list A list of text for options that should be created
        :return A dictionary mapping every option surface to its relevant rectangle
        """
        options = {}
        for index, option in enumerate(option_list):
            option_text = self.font.render(option, 1, self.text_color)
            option_rect = option_text.get_rect()
            option_rect.x = self.width/2 - option_rect.width/2
            option_rect.y = self.height/2 - option_rect.height/2
            options[option_text] = option_rect
        return options

    def render(self):
        """
        Render menu options
        """
        for option in self.menu_options:
            self.background.blit(option, self.menu_options[option])
