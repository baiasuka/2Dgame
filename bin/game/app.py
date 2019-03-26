import pygame
from pygame.locals import *
from sys import exit
import socket
import threading

from bin.game.materials import Pic

# ---------初始化----------
pygame.init()

# 定义窗口大小
screen = pygame.display.set_mode((1024, 768), 0, 32)
pygame.display.set_caption('Welcome!')

# 加载并转换图像
background = pygame.image.load(Pic.BACKGROUND_IMAGE).convert()
mouse_cursor = pygame.image.load(Pic.MOUSE_IMAGE).convert_alpha()
player_image = pygame.image.load(Pic.PLAYER_IMAGE).convert_alpha()

player_rect = pygame.Rect(800,500,97,109)


# 创建时钟对象
clock = pygame.time.Clock()


# ---------游戏循环----------
while True:
    # 设置刷新频率
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_rect.y -= 10
            elif event.key == pygame.K_s:
                player_rect.y += 10
            elif event.key == pygame.K_a:
                player_rect.x -= 10
            elif event.key == pygame.K_d:
                player_rect.x += 10


    # 绘制背景图
    screen.blit(background, (0, 0))

    # 获取鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算光标左上角位置
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    # 绘制鼠标
    screen.blit(mouse_cursor, (x, y))

    # 绘制玩家
    if player_rect.y < 0:
        player_rect.y = 768
    screen.blit(player_image, (player_rect.x,player_rect.y))

    pygame.display.update()
