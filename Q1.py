import turtle
import math
# 2D에서의 회전 변환 https://gaussian37.github.io/math-la-rotation_matrix/ 참고

def Arrow(Begin, End, t, Angle=30.):
    c_point = ((End[0] - Begin[0]) * -0.1, (End[1] - Begin[1]) * -0.1)
    c_Angle = Angle / 180. * math.pi
    c_leftPoint = (End[0]+c_point[0] * math.cos(c_Angle) - c_point[1] * math.sin(c_Angle), End[1]+c_point[0] * math.sin(c_Angle) + c_point[1] * math.cos(c_Angle))
    c_rightPoint = (End[0]+c_point[0] * math.cos(-c_Angle) - c_point[1] * math.sin(-c_Angle), End[1]+c_point[0] * math.sin(-c_Angle) + c_point[1] * math.cos(-c_Angle))
    t.penup()
    t.goto(Begin[0], Begin[1])
    t.pendown()
    t.goto(End[0], End[1])
    t.goto(c_leftPoint[0], c_leftPoint[1])
    t.goto(End[0], End[1])
    t.goto(c_rightPoint[0], c_rightPoint[1])

def Draw_event(x, y):
    global start_point
    if(start_point is None):
        start_point = (x,y)
    else:
        end_point = (x,y)
        t = turtle.Turtle()
        t.speed(0)
        arrow = Arrow(start_point, end_point, t)

        start_point = None

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('white')
start_point = None
end_point = None
turtle.onscreenclick(Draw_event)
turtle.done()

