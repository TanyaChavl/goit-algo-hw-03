import turtle

def koch_curve(t, iterations, length):
    if iterations == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, iterations - 1, length)
        t.left(60)
        koch_curve(t, iterations - 1, length)
        t.right(120)
        koch_curve(t, iterations - 1, length)
        t.left(60)
        koch_curve(t, iterations - 1, length)

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Koch Snowflake")

t = turtle.Turtle()
t.speed(0) 

# Тут можна встановити рівень рекурсії
recursion_level = int(5)

t.up()
t.goto(-150, 90)
t.down()

for i in range(3):
    koch_curve(t, recursion_level, 300)
    t.right(120)

t.hideturtle()
screen.mainloop()
