import random

import pygame


class Animal(pygame.sprite.Sprite):
    def __init__(self, environment):
        super().__init__()
        self.height = environment.get_height()
        self.width = environment.get_width()
        self.x_move = 0
        self.y_move = 0
        self.rotation = 0
        self.root_image = pygame.image.load("media/Mouse.png")
        self.image = self.root_image
        self.rect = self.root_image.get_rect()

    def _adjust_bearing(self):
        expected_rotation = self._expected_bearing()
        if expected_rotation != self.rotation:
            self.image = pygame.transform.rotate(self.root_image, expected_rotation)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rotation = expected_rotation

    def _expected_bearing(self):
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
        self.move()

    def move(self):
        """
        Moves the mouse and changes direction if it hits a wall
        :return:
        """
        self.rect.move_ip(self.x_move, self.y_move)


class Cat(Animal):
    """
    Cat that will chase mice
    """
    def __init__(self, environment):
        """
        Creates the cat
        :return:
        """
        super().__init__(environment)
        self.root_image = pygame.image.load("media/Cat.png")
        self.image = self.root_image
        self.rect = self.root_image.get_rect()

    def process_movement(self, input_event):
        if input_event.type == pygame.KEYUP:
            if input_event.key == pygame.K_UP or input_event.key == pygame.K_DOWN:
                self.y_move = 0
            elif input_event.key == pygame.K_LEFT or input_event.key == pygame.K_RIGHT:
                self.x_move = 0
            self._adjust_bearing()
        elif input_event.type == pygame.KEYDOWN:
            if input_event.key == pygame.K_UP:
                self.y_move = -2
            elif input_event.key == pygame.K_DOWN:
                self.y_move = 2
            elif input_event.key == pygame.K_LEFT:
                self.x_move = -2
            elif input_event.key == pygame.K_RIGHT:
                self.x_move = 2
            self._adjust_bearing()


class Mouse(Animal):
    """
    A Mouse that will scurry around a screen
    """
    def __init__(self, environment):
        """

        :param environment:
        :return:
        """
        super().__init__(environment)
        self.root_image = pygame.image.load("media/Mouse.png")
        self.image = self.root_image
        self.rect = self.root_image.get_rect()
        self.is_dead = False

    def move(self):
        """
        Moves the mouse and changes direction if it hits a wall
        :return:
        """
        if not self.is_dead:
            self._adjust_bearing()
            self.rect.move_ip(self.x_move, self.y_move)
            if self.rect.left < 0:
                self.x_move = -self.x_move
            elif self.rect.right > self.width:
                self.x_move = -1
            if self.rect.top < 0:
                self.y_move = 1
            elif self.rect.bottom > self.height:
                self.y_move = -1
            if self.x_move == 0:
                self.x_move = random.randint(-1, 1)
            if self.y_move == 0:
                self.y_move = random.randint(-1, 1)

    def die(self):
        """
        Causes the mouse to show up as dead
        :return:
        """
        self.image = pygame.transform.rotate(
            pygame.image.load("media/DeadMouse.png"),
            self.rotation)
        self.is_dead = True
