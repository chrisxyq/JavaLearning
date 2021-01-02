"""
# @author chrisxu
# @create 2020-08-03 15:56
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""


def compute(n, k):
    if k == 1 or n < k:
        return -1
    else:
        initer = inite(n)
        res = adjust(initer, k)
        return res


def inite(n):
    res = ''
    for i in range(n):
        if i % 2 == 0:
            res += 'a'
        else:
            res += 'b'
    return res


def adjust(initer, k):
    print(k)
    res=''
    if k > 2:
        myList=[]
        for ele in initer:
            myList.append(ele)
        for i in range(len(initer) - 1, len(initer) - 1 - (k - 2)+1, -1):
            if k - 2 - (1 + len(initer) - i)>=0:
                temp=myMap[str(k - 2 - (1 + len(initer) - i))]
                myList[i] = temp
        for ele in myList:
            res+=ele
    return res


if __name__ == '__main__':
    myMap = {'1': 'a', '2': 'b', '3': 'c', '4': 'd',
             '5': 'e', '6': 'f', '7': 'g', '8': 'h',
             '9': 'i', '10': 'j', '11': 'k', '12': 'l',
             '13': 'm', '14': 'n', '15': 'o', '16': 'p',
             '17': 'q', '18': 'r', '19': 's', '20': 't',
             '21': 'u', '22': 'v', '23': 'w', '24': 'x',
             '25': 'y', '26': 'z'
             }
    n, k = [int(i) for i in input().split()]
    res = compute(n, k)
    print(res)
