import random
from math import atan2, degrees

from pygame import image, transform, sprite


class Animal(sprite.Sprite):
    """
    An animal in the game
    """
    def __init__(self, environment, _speed):
        """
        Create an animal
        :param environment: The environment the animal lives in
        :param _speed: _speed of the animal
        """
        super().__init__()

        image_name = "media/Mouse.png"
        self._root_image = transform.rotate(image.load(image_name), 180)
        self.image = self._root_image
        self._height = environment.get_height()
        self._width = environment.get_width()
        self.rect = self._root_image.get_rect()
        self.rect.x = random.randrange(self._width)
        self.rect.y = random.randrange(self._height)
        self.is_dead = False

        self._speed = _speed
        self._wall_modifier = -1
        self._x_move, self._y_move, self._rotation = 0, 0, 0

    def _adjust_bearing(self):
        """
        Make the image the face the correct angle
        """
        expected_rotation = self._expected_bearing()
        if expected_rotation != self._rotation:
            self.image = transform.rotate(self._root_image, expected_rotation)
            self.rect = self.image.get_rect(center=self.rect.center)
            self._rotation = expected_rotation

    def _expected_bearing(self):
        """
        Find the bearing in degrees that an animal should face, S0 being west
        :return: the bearing of the animals
        """
        if self._x_move != 0 or self._y_move != 0:
            return -degrees(atan2(self._y_move, self._x_move))
        else:
            return self._rotation

    def update(self):
        """
        Move the animal on update
        """
        self.move()

    def move(self):
        """
        Moves the animal and change direction if it hits a wall
        """
        if not self.is_dead:
            self.rect.move_ip(self._x_move, self._y_move)
            if self.rect.left < 0 or self.rect.right > self._width:
                self._x_move *= self._wall_modifier
                if self.rect.left < 0:
                    self.rect.x = 0
                else:
                    self.rect.right = self._width
            if self.rect.top < 0 or self.rect.bottom > self._height:
                self._y_move *= self._wall_modifier
                if self.rect.top < 0:
                    self.rect.y = 0
                else:
                    self.rect.bottom = self._height
