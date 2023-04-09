from random import random, choice
import keyboard
from pygame import sprite
from pygame import key, K_LEFT, K_RIGHT

WhiteColor = (255, 255, 255)
import pygame
import sys
from pygame import transform
pygame.init()
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ping Pong Game")
fon = pygame.image.load('fon.png')
fon.set_colorkey(WhiteColor)
fon = transform.scale(fon, (display_width, display_height))

player_image = pygame.image.load("player.png")
player_image.set_colorkey(WhiteColor)
player_image = transform.scale(player_image, (30, 200))
player_width = player_image.get_width()
player_height = player_image.get_height()
player_x = display_width - player_width - 10
player_y = display_height / 2 - player_height / 2

enemy_image = transform.scale(player_image, (30, 200))
enemy_width = enemy_image.get_width()
enemy_height = enemy_image.get_height()
enemy_x = 10
enemy_y = display_height / 2 - enemy_height / 2

ball_image = pygame.image.load("ball.png")
ball_image.set_colorkey(WhiteColor)
ball_image = transform.scale(ball_image, (50, 50))

ball_width = ball_image.get_width()
ball_height = ball_image.get_height()
ball_x = display_width / 2 - ball_width / 2
ball_y = display_height / 2 - ball_height / 2
player_speed = 5
enemy_speed = 5
ball_speed = 5
ball_x_speed = ball_speed
ball_y_speed = ball_speed
move_right = False
move_left = False
player_score = 0
enemy_score = 0
move2_right = False
move2_left = False
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

class GameObj(sprite.Sprite):
    def __init__(self, x1=0, y1=0, width=10, height=10, filename='', moveP=True):
        super().__init__()
        self.moveP = moveP
        self.rect = pygame.Rect(x1, y1, width, height)
        self.picture = pygame.image.load(filename)  # load image

    def spawn(self):
        self.picture = transform.scale(self.picture, (self.rect.width, self.rect.height))
        self.picture.set_colorkey(WhiteColor)
        game_display.blit(self.picture, (self.rect.x, self.rect.y))  # blit image

    def collidepoint(self, x, y):  # collidepoint function
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)  # colliderect

player = GameObj(player_x, player_y, player_width, player_height, 'player.png')
enemy = GameObj(enemy_x, enemy_y, enemy_width, enemy_height, 'player.png')
ball = GameObj(ball_x, ball_y, ball_width, ball_height, 'ball.png')
def update_score():
    font2 = pygame.font.SysFont(None, 50)
    player_score_text = font2.render(str(player_score), True, (0, 170, 0))
    enemy_score_text = font2.render(str(enemy_score), True, (255, 255, 255))

    game_display.blit(player_score_text, (display_width / 2 + 50, 50))
    game_display.blit(enemy_score_text, (display_width / 2 - 50, 50))


while True:
    game_display.blit(fon, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:  # button press
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True

            if event.key == pygame.K_a:
                move2_right = True
            if event.key == pygame.K_d:
                move2_left = True
        elif event.type == pygame.KEYUP:  # button up
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_a:
                move2_right = False
            if event.key == pygame.K_d:
                move2_left = False

    if move2_left and enemy.rect.y < display_width-10:
        enemy.rect.y += 10
    if move2_right and enemy.rect.y > 10:
        enemy.rect.y -= 10
    if move_right:
        player.rect.y += player_speed
    if move_left:
        player.rect.y -= player_speed
    ball.rect.x += ball_x_speed
    ball.rect.y += ball_y_speed

    if ball.rect.y < 0 or ball.rect.y + ball.rect.height > display_height:
        ball_y_speed = -ball_y_speed
    if ball.rect.x < 0 or ball.rect.x + ball.rect.width > display_width:
        ball_x_speed = -ball_x_speed

    if ball.rect.x < 0:
        player_score += 1
        ball.rect.x = display_width / 2 - ball.rect.width / 2
        ball.rect.y = display_height / 2 - ball.rect.height / 2
        ball_y_speed = ball_speed * choice([-1, 1])
        ball_x_speed = ball_speed

    if ball.rect.x > display_width-player_width-40:
        enemy_score += 1
        ball.rect.x = display_width / 2 - ball.rect.width / 2
        ball.rect.y = display_height / 2 - ball.rect.height / 2
        ball_y_speed = ball_speed * choice([-1, 1])
        ball_x_speed = ball_speed


    if ball.colliderect(player):
        ball_x_speed = ball_speed * choice([-1, 1])
        ball_y_speed = ball_speed
    if ball.colliderect(enemy):
        ball_x_speed = ball_speed * choice([-1, 1])
        ball_y_speed = ball_speed


    player.spawn()
    enemy.spawn()
    ball.spawn()
    win_text = font.render("Win", True, (255, 255, 255))
    lose_text = font.render("Lose", True, (255, 255, 255))
    if enemy_score >= 11 or player_score >= 11:
        player_speed = 0
        ball_speed = 0
        enemy_speed = 0
        move_left = 0
        move2_right = 0
        move_right = 0
        move2_left = 0
        if enemy_score >= 11:
            game_display.blit(win_text, (75, 50))
            game_display.blit(lose_text, (display_width-150, 50))
        if player_score >= 11:
            game_display.blit(win_text, (display_width-75, 50))
            game_display.blit(lose_text, (75, 50))

    update_score()
    pygame.display.update()
    clock.tick(60)