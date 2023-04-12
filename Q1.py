import turtle
import math
# # 1. 화살표 시작점과 끝점을 연결한 선분
# # 2. 연결한 선분의 1/10 정도로 만든후 cos, sin을 이용하여 회전
# # 3. 완성된 좌표에서 수직으로 내림

def Arrow(Begin, End, t,Angle = 20.):
    c_Angle = (180 - Angle) / 180. * math.pi # 라디안 값 변환
    c_start = ((End[0] - Begin[0]) * (9. / 10.), (End[1] - Begin[1]) * (9. / 10.))
    c_r = math.sqrt((End[0] - Begin[0]) ** 2 + (End[1] - Begin[1]) ** 2) * 0.1
    print(c_r)

    c_leftPoint = (c_start[0] + c_r * math.cos(c_Angle), c_start[1] + c_r * math.sin(c_Angle))
    c_rightPoint = (c_start[0] + c_r * math.sin(c_Angle), c_start[1] + c_r * math.cos(c_Angle))
    print(c_leftPoint)
    print(c_rightPoint)


    t.penup()
    t.goto(Begin[0], Begin[1])
    t.pendown()
    t.goto(End[0], End[1])
    t.goto(c_leftPoint[0], c_leftPoint[1])
    t.goto(End[0], End[1])
    t.goto(c_rightPoint[0], c_rightPoint[1])
    # t.pendown()
    # t.goto(c_RightPoint[0], c_RightPoint[1])

    # t.pendown()

def Draw_event(x, y):
    global start_point
    if(start_point is None):
        start_point = (x,y)
    else:
        end_point = (x,y)
        t = turtle.Turtle()
        t.speed(0)
        arrow = Arrow((0,0), (-100,100), t, Angle=20)
        arrow = Arrow((0, 0), (100, 100), t, Angle=20)
        arrow = Arrow((0, 0), (-100, -100), t, Angle=20)
        arrow = Arrow((0, 0), (100, -100), t, Angle=20)
        start_point = None

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('white')
start_point = None
end_point = None
turtle.onscreenclick(Draw_event)
turtle.done()
#
# import turtle
# import math
#
# class SC_Arrow:
#     def __init__(self, Begin, End, pDC, Angle=20.):
#         self.sc_Begin = Begin
#         self.sc_End = End
#         self.sc_Angle = Angle / 180 * math.pi
#
#         self.sc_Increasement = ((self.sc_End[0] - self.sc_Begin[0]) * (-1. / 10.),
#                                 (self.sc_End[1] - self.sc_Begin[1]) * (-1. / 10.))
#
#         self.sc_LeftPoint = (math.cos(self.sc_Angle) * self.sc_Increasement[0] - math.sin(self.sc_Angle) * self.sc_Increasement[1],
#                              math.sin(self.sc_Angle) * self.sc_Increasement[0] + math.cos(self.sc_Angle) * self.sc_Increasement[1])
#         self.sc_LeftPoint = (self.sc_LeftPoint[0] + self.sc_End[0], self.sc_LeftPoint[1] + self.sc_End[1])
#
#         self.sc_RightPoint = (math.cos(self.sc_Angle) * self.sc_Increasement[0] + math.sin(self.sc_Angle) * self.sc_Increasement[1],
#                               -math.sin(self.sc_Angle) * self.sc_Increasement[0] + math.cos(self.sc_Angle) * self.sc_Increasement[1])
#         self.sc_RightPoint = (self.sc_RightPoint[0] + self.sc_End[0], self.sc_RightPoint[1] + self.sc_End[1])
#
#         self.pDC = pDC
#
#         self.pDC.penup()
#         self.pDC.goto(self.sc_Begin[0], self.sc_Begin[1])
#         self.pDC.pendown()
#         self.pDC.goto(self.sc_End[0], self.sc_End[1])
#         self.pDC.goto(self.sc_LeftPoint[0], self.sc_LeftPoint[1])
#         self.pDC.penup()
#         self.pDC.goto(self.sc_End[0], self.sc_End[1])
#         self.pDC.pendown()
#         self.pDC.goto(self.sc_RightPoint[0], self.sc_RightPoint[1])
#
# # 화면 초기화
# screen = turtle.Screen()
# screen.setup(800, 600)
# screen.bgcolor("white")
#
# # 마우스 클릭 이벤트 핸들러
# def get_coordinate(x, y):
#     global start_point
#     if start_point is None:
#         start_point = (x, y)
#     else:
#         end_point = (x, y)
#         t = turtle.Turtle()
#         t.speed(0)
#         arrow = SC_Arrow(start_point, end_point, t, Angle=20.)
#         start_point = None
#
# # 전역 변수 초기화
# start_point = None
#
# # 마우스 클릭 이벤트 등록
# turtle.onscreenclick(get_coordinate)
#
# # 화면 유지
# turtle.done()