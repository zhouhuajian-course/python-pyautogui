"""
pyautogui 消息对话框

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import alert, confirm, prompt, password
from pymsgbox import STOP, WARNING, TIMEOUT_RETURN_VALUE, ABORT_TEXT, RETRY_TEXT, IGNORE_TEXT, CANCEL_TEXT, TRY_AGAIN_TEXT, CONTINUE_TEXT, YES_TEXT, NO_TEXT
from tkinter import Tk, Button

"""
主要内容：
1. alert()    - 警告对话框；
2. confirm()  - 确认对话框；
3. prompt()   - 提示用户输入对话框；
4. password() - 密码输入对话框。
"""


def test_alert():
    """
    警告对话框

    返回被点击按钮的文本
    """
    # print(alert())  # 点确定、关闭都是返回"OK"，作者没做国际化
    # 源码 (TODO: for internationalization, change these)
    # print(alert(title="警告", text="自动化出现异常", icon=STOP))
    # print(alert(title="警告", text="自动化出现异常", icon=WARNING))

    # print(alert(title="警告", text="自动化出现异常", _tkinter=True))
    # print(alert(title="警告", text="自动化出现异常", button="已收到警告"))
    # print(alert(title="警告", text="自动化出现异常", button="已收到警告", timeout=3000))
    """
    注意点：
    点确定和关闭都是返回按钮文本"已收到警告"
    超时返回值是TIMEOUT_RETURN_VALUE = "Timeout"
    timeout用的是tkinter的after定时器，单位是毫秒
    """

    root = Tk()
    root.title("自动化控制台")

    def start_auto_gui_1():
        """开始#1UI自动化"""
        print(alert(title="警告", text="自动化出现异常", button="已收到警告", root=root))

    Button(root, text="开始#1", command=start_auto_gui_1).pack(pady=10)
    Button(root, text="开始#2").pack(pady=10)
    Button(root, text="开始#3").pack(pady=10)
    root.mainloop()


# test_alert()


def test_confirm():
    """
    确认对话框

    返回被点击按钮的文本，关闭返回None
    """
    # print(confirm())  # OK Cancel
    # print(confirm(title="请确认", text="是否继续？",  buttons=[ABORT_TEXT, RETRY_TEXT, IGNORE_TEXT]))
    # print(confirm(title="请确认", text="是否继续？",  buttons=[YES_TEXT, NO_TEXT, CANCEL_TEXT]))
    # print(confirm(title="请确认", text="是否继续？",  buttons=["继续", "不继续"]))

    # print(confirm(title="请确认", text="是否继续？", buttons=["继续", "不继续"], timeout=3000))


test_confirm()


def test_prompt():
    """
    提示用户输入对话框

    返回输入的文本，如果取消或关闭，返回None
    """
    # print(prompt())
    # print(prompt(title="运行次数", text="请输入多少次？", default="3"))

    # 超时返回Timeout而不是默认值
    # print(prompt(title="运行次数", text="请输入要跑多少次？", default="3", timeout=3000))


test_prompt()


def test_password():
    """
    密码输入对话框

    返回输入的文本，如果取消或关闭，返回None
    """
    # print(password())
    # print(password(title="密码", text="请输入密码", default="123456"))
    # print(password(title="密码", text="请输入密码", default="123456", mask="#"))

    # 超时返回Timeout而不是默认值
    print(password(title="密码", text="请输入密码", default="123456", mask="#", timeout=3000))


test_password()
