"""
# @author chrisxu
# @create 2020-08-15 18:50
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""
nums = [int(i) for i in input().split()]
tar = int(input())

def get_time(treenode):
    if "end" in treenode.node:
        return treenode.time
    else:
        for ele in