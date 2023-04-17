# 원의 방정식으로 접근
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
def Get_gradient(x1, y1, x2, y2):
    gradient = (y1 - y2) / (x1 - x2)
    return gradient

def Get_upperPoint(gradient,length,x1,y1):
    vertical_gradient = -1. / gradient
    # y절편
    y_ = y1 - vertical_gradient * x1
    x = x1 + math.sqrt(length ** 2 * gradient ** 2 / (gradient ** 2 + 1))
    x_ = x1 - math.sqrt(length ** 2 * gradient ** 2 / (gradient ** 2 + 1))
    print('x : ', x)
    print('x_ : ', x_)
    if(x < x_):
        print('경우가 있음')
    y = vertical_gradient*(x - x1) + y1

    return x, y


def Get_downPoint(gradient,length,x1,y1):
    vertical_gradient = -1. / gradient
    # y절편
    x = x1 - math.sqrt(length ** 2 * gradient ** 2 / (gradient ** 2 + 1))
    y = vertical_gradient*(x - x1) + y1
    return x,y



# 시간에 따른 랜덤한 값들 생성
np.random.seed(0)  # 랜덤 시드 고정
num_points = 1000  # 생성할 점의 개수
time = np.linspace(0, 10, num_points)  # 0부터 10까지의 시간 생성
y_points = np.random.randn(num_points).cumsum()  # 랜덤한 값들의 누적합 계산
upper_x = []
upper_y = []
down_x = []
down_y = []
# 기울기
gradient = 0
# 간격
length = 0.05
for i in range(len(time)):
    try:
        gradient = Get_gradient(time[i], y_points[i], time[i+1], y_points[i+1])
        x,y  = Get_upperPoint(gradient, length, time[i], y_points[i])
        x_,y_ = Get_downPoint(gradient, length, time[i], y_points[i])
        upper_x.append(x)
        upper_y.append(y)
        down_x.append(x_)
        down_y.append(y_)
    except:
        print("초과")

print(len(upper_x))
# 그래프 그리기

plt.plot(time, y_points, '-')  # 연속적인 그래프 그리기
plt.plot(upper_x, upper_y, '-')
plt.plot(down_x, down_y, '-')
plt.xlabel('시간')  # X축 레이블 설정
plt.ylabel('값')  # Y축 레이블 설정
plt.title('시간에 따른 연속적인 그래프와 영역 색칠')  # 그래프 제목 설정
plt.grid(True)  # 그리드 표시
plt.show()  # 그래프 출력