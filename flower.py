from turtle import *
import colorsys

speed(0)
bgcolor("Black")

i = 0
for k in range(15):
    for j in range(6):
        c = colorsys.hsv_to_rgb(i, 1, 1)
        color(c)
        i += 0.005
        rt(90)
        circle(150 - j * 8, 90)
        lt(90)
        circle(150 - j * 8, 90)
        rt(180)
    circle(40, 24)
