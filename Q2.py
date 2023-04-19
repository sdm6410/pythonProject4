# 원의 방정식으로 접근
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def circle_point(center_x, center_y, coord_x, r):
    upper_y = 0
    down_y = 0
    try:
        if coord_x < center_x - r or coord_x > center_x + r:
            raise ValueError('Coord_x is out of circlue range.')
        y = center_y + math.sqrt(r ** 2 - (coord_x-center_x) ** 2)
        y_ = center_y - math.sqrt(r ** 2 - (coord_x-center_x) ** 2)
    except ValueError:
        y = math.nan
        y_ = math.nan
    if(y > y_):
        upper_y = y
        down_y = y_
    else:
        down_y = y
        upper_y = y_

    return upper_y, down_y


font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 시간에 따른 랜덤한 값들 생성
np.random.seed(0)  # 랜덤 시드 고정
num_points = 100  # 생성할 점의 개수
time = np.arange(0, 100)  # 0부터 10까지의 시간 생성
y_points = np.random.randn(num_points).cumsum()  # 랜덤한 값들의 누적합 계산


# 간격
length = 2
theta = np.linspace(0, 2 * np.pi, 100)

upper_y = [-math.inf for i in range(len(time)+length)]
down_y = [math.inf for j in range(len(time) + length)]
for i in range(len(time)):
    try:
        for j in range(int(time[i] - length), int(time[i] + length)):
            print('j :', j)
            print(circle_point(time[i], y_points[i],j,length))
            if(j < 0):
                continue
            if(upper_y[j] < circle_point(time[i], y_points[i],j,length)[0]):
                upper_y[j] = circle_point(time[i], y_points[i],j,length)[0]
            if(down_y[j] > circle_point(time[i], y_points[i],j,length)[1]):
                down_y[j] = circle_point(time[i], y_points[i],j,length)[1]


        c_x = time[i] + length * np.cos(theta)
        c_y = y_points[i] + length * np.sin(theta)
        plt.axis('equal')
        plt.plot(c_x, c_y, '-')

    except Exception as err:
        print({err})



plt.plot(time, y_points, '-')  # 연속적인 그래프 그리기
plt.plot(time, upper_y[0:len(time)], '-')
plt.plot(time, down_y[0:len(time)], '-')
plt.xlabel('시간')  # X축 레이블 설정
plt.ylabel('값')  # Y축 레이블 설정
plt.title('시간에 따른 연속적인 그래프와 영역 색칠')  # 그래프 제목 설정
plt.grid(True)  # 그리드 표시
plt.show()  # 그래프 출력