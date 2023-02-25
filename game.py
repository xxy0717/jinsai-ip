import streamlit as st
import numpy as np
import time

# 导入你的游戏代码和依赖
from sheshe import *

# 设置游戏区域的大小和方格的大小
GRID_SIZE = 20
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# 初始化游戏区域和当前方块
game_board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=np.int32)
current_tetromino = get_random_tetromino()

# 记录游戏是否结束
game_over = False

# 用于控制游戏速度的时间间隔
game_speed = 0.5

# 绘制游戏区域
def draw_game_board(game_board):
    for i in range(game_board.shape[0]):
        for j in range(game_board.shape[1]):
            if game_board[i, j] != 0:
                st.markdown(f'<div style="background-color:{TETROMINO_COLORS[game_board[i, j]]}; height:{GRID_SIZE}px; width:{GRID_SIZE}px; display:inline-block;"></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="background-color:gray; height:{GRID_SIZE}px; width:{GRID_SIZE}px; display:inline-block;"></div>', unsafe_allow_html=True)
    st.write("")

# 游戏循环
while not game_over:

    # 清空输出区域
    st.empty()

    # 检查是否可以移动当前方块
    can_move_down = check_if_tetromino_can_move_down()
    can_move_left = check_if_tetromino_can_move_left()
    can_move_right = check_if_tetromino_can_move_right()

    # 绘制游戏区域和当前方块
    draw_game_board(game_board)
    draw_tetromino(current_tetromino, game_board)

    # 显示控制按钮
    st.write("")

    if st.button("向左移动") and can_move_left:
        move_tetromino_left()
    if st.button("向右移动") and can_move_right:
        move_tetromino_right()
    if st.button("向下移动") and can_move_down:
        move_tetromino_down()
    if st.button("旋转方块"):
        rotate_tetromino()

    # 移动当前方块并更新游戏区域
    if can_move_down:
        move_tetromino_down()
    else:
        add_tetromino_to_board()
        remove_completed_rows()
        current_tetromino = get_random_tetromino()

        if check_if_game_over():
            game_over = True

    # 等待一段时间，控制游戏速度
    time.sleep(game_speed)

# 游戏结束
st.write("游戏结束")
