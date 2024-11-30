import turtle

# 设置画布和画笔
screen = turtle.Screen()
star_turtle = turtle.Turtle()

# 设置画笔速度
star_turtle.speed(5)

# 画五角星的函数
def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)  # 五角星的内角是36度，所以外角是144度

# 画五角星
draw_star(100)

# 隐藏画笔的箭头
star_turtle.hideturtle()

# 保持窗口
screen.mainloop()