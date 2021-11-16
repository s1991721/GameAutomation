import os
import time


def checkTeam():
    # 菜单栏开关
    menu = '40.08789 71.4386'
    # 队伍
    team = '170.50781 278.25623'
    # 自动匹配
    matching = '1285.2051 130.35278'
    # 关闭
    close = '1385.498 46.417236'

    os.system(cmd.format(menu))
    time.sleep(1)
    os.system(cmd.format(team))
    time.sleep(1)
    os.system(cmd.format(matching))
    time.sleep(1)
    os.system(cmd.format(close))


if __name__ == '__main__':
    print('start goast')

    a = 1
    cmd = "adb shell input tap {}"

    # 任务栏
    mission = '1470.8008 261.969'
    # 开启下一轮
    continueNext = '934.13086 500.09766'
    # 领取任务
    accept = '1456.9824 327.1454'

    while (a < 10):
        # 单击任务
        print('单击任务')
        os.system(cmd.format(mission))
        time.sleep(30)
        # 下一轮
        print('下一轮')
        os.system(cmd.format(continueNext))
        time.sleep(15)
        # 领取任务
        print('领取任务')
        os.system(cmd.format(accept))
        time.sleep(15)
        checkTeam()
