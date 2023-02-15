import pygame
import random

# 初始化 Pygame 库
pygame.init()

# 设置游戏窗口大小
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 定义贪吃蛇和食物的大小和位置
snake_size = 10
snake_x, snake_y = 100, 100
food_x, food_y = random.randint(0, width), random.randint(0, height)

# 设置游戏循环
game_over = False
while not game_over:
    # 检查游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 清屏
    screen.fill((255, 255, 255))

    # 绘制贪吃蛇和食物
    pygame.draw.rect(screen, (0, 255, 0), (snake_x, snake_y, snake_size, snake_size))
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, snake_size, snake_size))

    # 更新屏幕
    pygame.display.update()

    # 移动贪吃蛇
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= 10
    if keys[pygame.K_RIGHT]:
        snake_x += 10
    if keys[pygame.K_UP]:
        snake_y -= 10
    if keys[pygame.K_DOWN]:
        snake_y += 10

    # 检查贪吃蛇是否碰到食物
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = random.randint(0, width), random.randint(0, height)
        score += 10

    # 限制帧速率
    pygame.time.Clock().tick(30)

# 退出 Pygame 库
pygame.quit()
