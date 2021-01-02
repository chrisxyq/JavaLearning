"""
# @author chrisxu
# @create 2020-07-31 14:07
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法

付钱至少需要几张钱
5 2 2 3 4
501
"""


def func(nums, tar):
    if tar < 0 or tar > nums[0] + 5 * nums[1] + 10 * nums[2] + 50 * nums[3] + 100 * nums[4]:
        return -1
    if tar == 0:
        return 0
    if tar >= 100:
        nums[4] -= tar // 100
        return tar // 100 + func(nums, tar - 100 * (tar // 100))
    if tar >= 50:
        #print(tar//50)
        nums[3] -= tar //50
        return tar // 50 + func(nums, tar - 50 * (tar // 50))
    if tar >= 10:
        nums[2] -= tar // 10
        return tar // 10 + func(nums, tar - 10 * (tar // 10))
    if tar >= 5:
        nums[1] -= tar // 5
        return tar // 5 + func(nums, tar - 5 * (tar // 5))
    if tar < 5:
        return tar


nums = [int(i) for i in input().split()]
tar = int(input())
RMB = [1, 5, 10, 50, 100]
res=func(nums, tar)
print(res)
