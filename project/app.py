"""
pyautogui UI自动化 小项目

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import countdown, click, doubleClick, write, press, pixelMatchesColor, screenshot, alert, sleep, \
    getActiveWindow


def start_auto_gui():
    """
    1. 双击火狐；
    2. 等待火狐加载；
    3. 火狐窗口最大化；
    4. 点击搜索；
    5. 输入pyautogui；
    6. 搜索pyautogui；
    7. 等待搜索结果；
    8. 点击pyautogui文档；
    9. 屏幕截图。
    10. 提示UI自动化完成。
    """
    sleep_time = 1  # 通用暂停时间
    print("3秒后开始UI自动化")
    countdown(3)
    print("双击火狐")
    doubleClick("./image/firefox.png")
    #
    # # https://pypi.org/project/PyGetWindow/
    # # $ sleep(5); win = getActiveWindow(); win.title; win.maximize()
    print("等待火狐加载")
    while True:
        win = getActiveWindow()
        if win.title == "Mozilla Firefox":
            break
        sleep(sleep_time)

    print("火狐窗口最大化")
    win.maximize()
    sleep(sleep_time)

    print("点击搜索")
    click(292, 83)
    # 重试机制 搜索框青色边框
    # 223,63  33,143,166  #218FA6
    while not pixelMatchesColor(315, 62, (33, 143, 166), tolerance=5):
        click(292, 83)
        sleep(sleep_time)

    print("输入pyautogui")
    write("pyautogui", interval=0.5)
    #
    print("搜索pyautogui")
    press("enter", presses=2, interval=0.5)  # 两次enter，解决中文输入法问题
    sleep(sleep_time)
    #
    print("等待搜索结果")
    # 左上角微软Logo
    # 64,237 241,103,37 #F16725
    while not pixelMatchesColor(63, 246, (241, 100, 33), tolerance=5):
        sleep(sleep_time)
    #
    print("点击pyautogui文档")
    # 文档左上角蓝色颜色
    while not pixelMatchesColor(120, 197, (41, 128, 185), tolerance=5):
        click(547, 573)
        sleep(sleep_time)
    #
    print("屏幕截图")
    screenshot('./doc.png')
    #
    print("提示UI自动化完成")
    alert(title='提示', text='UI自动化已完成', timeout=10000)
    print("UI自动化已完成")


if __name__ == '__main__':
    start_auto_gui()
