import time

from pygame.font import Font


class PlayTextRenderer:
    """
    Renders and updates relevant text for playing the game
    """
    def __init__(self, screen, num_of_mice):
        """
        Setup relevant class variables and UI components to draw the score and timer
        :param screen: Surface which the game is played on
        :param num_of_mice: The number of mice involved in the game
        """
        self.text_color = (10, 10, 10)
        self.width, self.height = screen.get_size()
        self.background = screen
        self.total_mice = num_of_mice
        # Set the score display
        self.font = Font(None, 36)
        self.score = 0
        self.score_text = self.font.render(str(self.score), 1, self.text_color)
        self.score_pos = self.score_text.get_rect()
        self.score_pos.x = self.width/2

        # Set the time display
        self.start = time.time()
        self.end = self.start + (self.total_mice*2.5)
        self.time_text = self.font.render(str(self.start), 1, self.text_color)
        self.time_pos = self.time_text.get_rect()
        self.time_pos.x = self.width/2
        self.time_pos.y = self.height - self.time_pos.height

    def update_score(self):
        """
        Add one to the score and render the updated value
        """
        self.score += 1
        self.score_text = self.font.render(str(self.score), 1, self.text_color)

    def render(self):
        """
        Render the time and score
        """
        if self.total_mice - self.score > 0:
            self.time_text = self.font.render(str(self.end-time.time())[:4], 1, self.text_color)
        self.background.blit(self.score_text, self.score_pos)
        self.background.blit(self.time_text, self.time_pos)
