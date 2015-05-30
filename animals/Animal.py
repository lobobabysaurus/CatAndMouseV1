import random

from pygame import image, transform, sprite


class Animal(sprite.Sprite):
    """
    An animal in the game
    """
    def __init__(self, environment, speed):
        """
        Create an animal
        :param environment: The environment the animal lives in
        :param speed: Speed of the animal
        """
        super().__init__()
        self.image_name = "media/Mouse.png"
        self.speed = speed
        self.height = environment.get_height()
        self.width = environment.get_width()
        self.wall_modifier = -1
        self.x_move, self.y_move, self. rotation = 0, 0, 0
        self.root_image = image.load(self.image_name)
        self.image = self.root_image
        self.rect = self.root_image.get_rect()
        self.rect.x = random.randrange(self.width)
        self.rect.y = random.randrange(self.height)
        self.is_dead = False

    def _adjust_bearing(self):
        """
        Make the image the face the correct angle
        """
        expected_rotation = self._expected_bearing()
        if expected_rotation != self.rotation:
            self.image = transform.rotate(self.root_image, expected_rotation)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rotation = expected_rotation

    def _expected_bearing(self):
        """
        Find the bearing in degrees that an animal should face with 0 being west
        :return: the bearing of the animals
        """
        if self.x_move > 0:
            if self.y_move > 0:
                return 135
            elif self.y_move == 0:
                return 180
            else:
                return 235
        elif self.x_move == 0:
            if self.y_move > 0:
                return 90
            elif self.y_move == 0:
                return self.rotation
            else:
                return 270
        elif self.x_move < 0:
            if self.y_move > 0:
                return 45
            elif self.y_move == 0:
                return 0
            else:
                return 315

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
            self.rect.move_ip(self.x_move, self.y_move)
            if self.rect.left < 0 or self.rect.right > self.width:
                self.x_move *= self.wall_modifier
                if self.rect.left < 0:
                    self.rect.x = 0
                else:
                    self.rect.right = self.width
            if self.rect.top < 0 or self.rect.bottom > self.height:
                self.y_move *= self.wall_modifier
                if self.rect.top < 0:
                    self.rect.y = 0
                else:
                    self.rect.bottom = self.height
