"""
pyautogui 屏幕像素获取、屏幕像素匹配

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import pixel, pixelMatchesColor, screenshot

"""
主要内容：
1. pixel() - 获取屏幕像素；
2. pixelMatchesColor() - 屏幕像素匹配颜色。
"""


def test_pixel_pixelMatchesColor():
    """屏幕像素获取、屏幕像素匹配"""
    # img = screenshot()
    # print(img)
    # print(img.getpixel((44, 107)))
    # (149, 212, 234)

    # print(pixel(44, 107))

    # 根据上面返回值修改color
    # print(pixelMatchesColor(44, 107, (149, 212, 234)))
    # print(pixelMatchesColor(44, 107, (148, 212, 234)))

    # color简单调整
    print(pixelMatchesColor(44, 107, (148, 212, 234), tolerance=20))
    print(pixelMatchesColor(44, 107, (100, 212, 234), tolerance=20))

    # 看看小项目 重试、等待


test_pixel_pixelMatchesColor()
