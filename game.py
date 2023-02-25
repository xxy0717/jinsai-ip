import pygame
import random

# 初始化Pygame库
pygame.init()

# 定义屏幕大小
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义方块大小
BLOCK_SIZE = 20

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 定义方块类
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move_down(self):
        self.y += BLOCK_SIZE

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, BLOCK_SIZE, BLOCK_SIZE])

# 创建方块列表
blocks = []
for i in range(10):
    blocks.append(Block(random.randint(0, SCREEN_WIDTH-BLOCK_SIZE), random.randint(0, SCREEN_HEIGHT-BLOCK_SIZE)))

# 游戏循环
running = True
while running:
    # 事件循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充屏幕
    screen.fill(BLACK)

    # 绘制方块
    for block in blocks:
        block.move_down()
        block.draw()

        # 判断方块是否超出屏幕
        if block.y > SCREEN_HEIGHT:
            blocks.remove(block)
            blocks.append(Block(random.randint(0, SCREEN_WIDTH-BLOCK_SIZE), random.randint(-SCREEN_HEIGHT, -BLOCK_SIZE)))

    # 更新屏幕
    pygame.display.flip()

# 退出Pygame库
pygame.quit()
