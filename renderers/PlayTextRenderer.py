import time

from renderers import TextRenderer


class PlayTextRenderer(TextRenderer):
    """
    Renders and updates relevant text for playing the game
    """
    def __init__(self, screen, num_of_mice):
        """
        Setup relevant class variables and UI components to draw the  and timer
        :param screen: Surface which the game is played on
        :param num_of_mice: The number of mice involved in the game
        """
        super().__init__(screen)

        self._total_mice = num_of_mice
        # Set the score display
        self._score = 0
        self._score_text = self._font.render(
            str(self._score), 1, self._text_color)
        self._score_pos = self._score_text.get_rect()
        self._score_pos.x = self._width/2

        # Set the time display
        self._start = time.time()
        self._end = self._start + (self._total_mice*2.5)
        self._time_text = self._font.render(
            str(self._start), 1, self._text_color)
        self._time_pos = self._time_text.get_rect()
        self._time_pos.x = self._width/2
        self._time_pos.y = self._height - self._time_pos.height

    def update_score(self):
        """
        Add one to the score and render the updated value
        """
        self._score += 1
        self._score_text = self._font.render(
            str(self._score), 1, self._text_color)

    def render(self):
        """
        Render the time and score
        """
        if self._total_mice - self._score > 0:
            self._time_text = self._font.render(
                str(self._end-time.time())[:4], 1, self._text_color)
        self._background.blit(self._score_text, self._score_pos)
        self._background.blit(self._time_text, self._time_pos)
