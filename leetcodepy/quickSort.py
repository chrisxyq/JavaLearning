"""
# @author chrisxu
# @create 2020-09-26 13:04
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""


def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1
    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def quickSort(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quickSort(array, beg, pivot)
        quickSort(array, pivot + 1, end)


def test_quickSort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    quickSort(seq, 0, len(seq))
    print(seq)


test_quickSort()
