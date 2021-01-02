"""
# @author chrisxu
# @create 2020-08-03 15:06
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""


def initer(num):
    init = ''
    for ele in str(num):
        #print(ele)
        init += map[ele]
    #print(init)
    return init


def process(num):
    init = initer(num)
    if len(init)==4:
        return init[::-1]+'00000000'
    elif len(init)==8:
        return init[::-1] + '0000'
    else:
        return init[::-1]


if __name__ == '__main__':

    map = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
           '6': '0110', '7': '0111', '8': '1000', '9': '1001'}
    n = input()
    nums = [int(i) for i in input().split()]
    for num in nums:
        res = process(num)
        print(int(res))
