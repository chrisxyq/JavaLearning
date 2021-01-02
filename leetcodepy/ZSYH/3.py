"""
# @author chrisxu
# @create 2020-08-03 15:34
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""


def get_money(myList, money):
    max = sorted(myList)[-1]
    if max > 1:
        ele1 = max // 2
        ele2 = max // 2 + 1
        myList.pop(-1)
        myList.append(ele1)
        myList.append(ele2)
        money += ele1 * ele2
        return myList, money
    else:
        return 0, 0


def compute():
    res, money = 0, 0
    myList = [s]
    while money < m:
        myList, money = get_money(myList, money)
        if myList == 0:
            return -1
        res += 1
    return res


if __name__ == '__main__':
    s, m = [int(i) for i in input().split()]
    res = compute()
    print(res)
