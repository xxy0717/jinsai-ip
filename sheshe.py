import streamlit as st
from PIL import Image, ImageDraw
from io import BytesIO

# 游戏区域的大小
SIZE = 20

# 每个方格的像素大小
PIXEL = 20

# 初始的蛇和食物
snake = [(SIZE//2, SIZE//2)]
food = (0, 0)

# 蛇的初始移动方向
direction = 'right'

# 生成一个新的食物
def new_food():
    global food
    while True:
        x = random.randint(0, SIZE-1)
        y = random.randint(0, SIZE-1)
        if (x, y) not in snake:
            food = (x, y)
            break

# 判断蛇是否碰到了墙壁或自己的身体
def collide():
    x, y = snake[-1]
    if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
        return True
    if (x, y) in snake[:-1]:
        return True
    return False

# 更新蛇的位置和食物
def update():
    global snake, food, direction
    x, y = snake[-1]
    if direction == 'up':
        y -= 1
    elif direction == 'down':
        y += 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1
    if (x, y) == food:
        snake.append(food)
        new_food()
    else:
        snake.pop(0)
        snake.append((x, y))

# 绘制游戏区域
def draw_game():
    im = Image.new('RGB', (SIZE * PIXEL, SIZE * PIXEL), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i, (x, y) in enumerate(snake):
        color = (0, 255 - i * 5, 0)
        draw.rectangle((x * PIXEL, y * PIXEL, (x + 1) * PIXEL, (y + 1) * PIXEL), fill=color)
    draw.rectangle((food[0] * PIXEL, food[1] * PIXEL, (food[0] + 1) * PIXEL, (food[1] + 1) * PIXEL), fill=(255, 0, 0))
    return im

# 用 Streamlit 显示游戏界面
def show_game():
    col1, col2 = st.beta_columns([3, 1])
    with col1:
        st.image(draw_game(), use_column_width=True)
    with col2:
        st.markdown('**Score:** ' + str(len(snake) - 1))

# 重置游戏
def reset_game():
    global snake, food, direction
    snake = [(SIZE//2, SIZE//2)]
    direction = 'right'
    new_food()

# 主函数
def main():
    st.title('贪吃蛇')
    st.write('方向键或 WASD 控制蛇的移动，吃到红色的方块即可获得积分。')
    st.write('你的目标是尽
