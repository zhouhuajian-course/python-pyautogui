"""
pyautogui 鼠标控制函数

size()     - 获取屏幕分辨率
position() - 获取当前鼠标坐标
onScreen() - 判断一个坐标是否在屏幕上

@author  : zhouhuajian
@version : v1.0
"""

import collections

from pyautogui import size, position, onScreen

"""
主要内容：
1. 屏幕坐标系；
2. 命名元组、Size类和Point类；
3. size()     - 获取屏幕分辨率
4. position() - 获取当前鼠标坐标
5. onScreen() - 判断一个坐标是否在屏幕上
"""


def intro_namedtuple():
    """介绍命名元组"""
    # Point = collections.namedtuple("Point", "x y")
    # Size = collections.namedtuple("Size", "width height")
    # 屏幕分辨率大小
    screen_size = (1920, 1080)
    # 缺点 获取长宽可使用screen_size[0]、screen_size[1]，
    # 但不能直观地使用screen_size.width screen_size.height获取长宽
    # print(screen_size)
    # print(screen_size[0], screen_size[1])
    # print(screen_size.width, screen_size.height)
    # exit()
    print('----------')
    # Size = collections.namedtuple("Size", "width height")
    # screen_size = Size(1920, 1080)
    # print(screen_size)
    # print(screen_size[0], screen_size[1])
    # print(screen_size.width, screen_size.height)
    # exit()
    # 坐标点
    point = (100, 200)
    print('----------')
    # print(point)
    # print(point[0], point[1])
    # print(point.x, point.y)
    Point = collections.namedtuple("Point", "x y")
    point = Point(100, 200)
    print('----------')
    print(point)
    print(point[0], point[1])
    print(point.x, point.y)


# intro_namedtuple()


def test_size():
    """size() - 获取屏幕分辨率大小"""
    screen_size = size()
    print(screen_size)
    print(screen_size[0], screen_size[1])
    print(screen_size.width, screen_size.height)


# test_size()

def test_position():
    """position() - 获取当前鼠标坐标"""
    point = position()
    print(point)
    print(point[0], point[1])
    print(point.x, point.y)
    print('-----')
    print(position(x=100))
    print(position(y=100))
    print(position(x=100, y=100))


# test_position()


def test_onScreen():
    """onScreen() - 判断一个坐标是否在屏幕里面"""
    print(onScreen(0, 0))
    print(onScreen(1919, 1079))
    print(onScreen(-1, 0))
    print(onScreen(1920, 1079))
    # size()
    # 0 <= x < 1920
    # 0 <= y < 1080
    print('-----')
    print(onScreen([0, 0]))
    print(onScreen((1919, 1079)))


# test_onScreen()
