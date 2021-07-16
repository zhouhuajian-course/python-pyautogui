"""
pyautogui 图片定位

@author  : zhouhuajian
@version : v1.0
"""

import pyscreeze
import time
from pyautogui import locateOnScreen, center, locateCenterOnScreen, locateAllOnScreen, locate, locateAll, click, moveTo, \
    screenshot

"""
主要内容：
1. locateOnScreen() - 在屏幕上进行图片定位，返回图片区域；
2. center() - 返回图片区域的中心坐标点；
3. locateCenterOnScreen() - 在屏幕上进行图片定位，返回中心坐标点；
4. locateAllOnScreen() - 在屏幕上进行图片定位，返回所有图片区域；
5. locate() - 在给定图片上进行图片定位，返回图片区域；
6. locateAll() - 在给定图片上进行图片定位，返回所有图片区域；
7. click()、moveTo()等函数传图片路径。
"""


def test_locate():
    """图片定位"""
    """locateOnScreen 在屏幕上进行图片定位，返回图片区域"""
    # print(locateOnScreen('./image/firefox.png'))  # position 看图片大小简单对比Box结果
    # Point(x=12, y=450)
    # box = locateOnScreen('./image/firefox.png')
    # print(box[0], box[1], box[2], box[3])
    # print(box.left, box.top, box.width, box.height)

    # print(locateOnScreen('./image/python_file.png'))  # 返回None
    # 0.9.41之前，raise ImageNotFoundException
    # pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True
    # print(locateOnScreen('./image/python_file.png'))  # 抛异常

    # print(locateOnScreen('./image/python_file.png', minSearchTime=10))  # 重试机制

    # print(locateOnScreen('./image/firefox.png', confidence=0.9))  # 精确度
    # TypeError: _locateAll_python() got an unexpected keyword argument 'confidence'
    # pip install opencv-python

    # print(locateOnScreen('./image/firefox.png', grayscale=True))  # 灰度图 类似黑白照片
    # 准确度比较低 TODO: 下节课演示
    start = time.time()
    print(locateOnScreen('./image/github.png', grayscale=False))  # 灰度图 类似黑白照片
    print(time.time() - start)
    start = time.time()
    print(locateOnScreen('./image/github.png', grayscale=True))  # 灰度图 类似黑白照片
    print(time.time() - start)

    # print(locateOnScreen('./image/firefox.png'))
    # box = (7, 432, 113 - 7, 709 - 432)  # position
    # print(locateOnScreen('./image/firefox.png', region=box))

    """center"""
    # print(locateOnScreen('./image/firefox.png'))
    # print(center(locateOnScreen('./image/firefox.png')))
    # # Point(x=52, y=499)

    """locateCenterOnScreen"""
    # print(locateCenterOnScreen('./image/firefox.png'))

    """locateAllOnScreen"""
    # 复制firefox
    # print(locateAllOnScreen('./image/firefox.png'))
    # print(list(locateAllOnScreen('./image/firefox.png')))

    """locate"""
    needleImage = './image/firefox.png'
    haystackImage = './image/haystack.png'
    # print(locate(needleImage, haystackImage))
    # print(locateOnScreen('./image/firefox.png'))

    """locateAll"""
    # print(locateAll(needleImage, haystackImage))
    # print(list(locateAll(needleImage, haystackImage)))

    # click('./image/firefox.png')
    # moveTo('./image/firefox.png')
    # 复制的firefox移到chrome右边


test_locate()
