import streamlit as st
import time
import random

# 游戏画面参数
ROWS = 30
COLS = 30
CELL_SIZE = 20

# 食物颜色
FOOD_COLOR = (255, 0, 0)

# 蛇身颜色
SNAKE_COLOR = (0, 255, 0)

# 游戏界面背景颜色
BACKGROUND_COLOR = (0, 0, 0)

# 定义方向常量
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# 初始化游戏界面
game_board = [[0] * COLS for _ in range(ROWS)]

# 初始化蛇
snake = [(ROWS // 2, COLS // 2)]
snake_dir = RIGHT

# 初始化食物
food = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))

# 更新蛇的位置
def update_snake(snake, snake_dir):
    row, col = snake[0]

    if snake_dir == UP:
        row -= 1
    elif snake_dir == RIGHT:
        col += 1
    elif snake_dir == DOWN:
        row += 1
    else:
        col -= 1

    snake.insert(0, (row, col))
    return snake[:-1]

# 检查蛇是否吃到了食物
def check_food(snake, food):
    return snake[0] == food

# 更新食物的位置
def update_food(snake):
    while True:
        food = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
        if food not in snake:
            return food

# 检查蛇是否死亡
def check_death(snake):
    row, col = snake[0]
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        return True

    for i in range(1, len(snake)):
        if snake[i] == snake[0]:
            return True

    return False

# 画游戏界面
def draw_game_board(game_board, snake, food):
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) == food:
                st.square(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, FOOD_COLOR)
            elif (row, col) in snake:
                st.square(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, SNAKE_COLOR)
            else:
                st.square(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, BACKGROUND_COLOR)

# Streamlit应用程序
def app():
    st.title("贪吃蛇游戏")

    while True:
        # 游戏界面
        draw_game_board(game_board, snake, food)

        # 更新蛇的位置
        snake = update_snake(snake, snake_dir)

        # 如果蛇吃到了食物，更新食物的位置
        if check_food(snake, food):
