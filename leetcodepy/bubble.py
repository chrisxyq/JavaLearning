"""
# @author chrisxu
# @create 2020-09-26 14:51
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""
import random


def bubble(mylist):
    #i, j = 0, 1
    for i in range(len(mylist)):
        for j in range(0, len(mylist)-i - 1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]


def test_bubble():
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    bubble(seq)
    print(seq)


test_bubble()
