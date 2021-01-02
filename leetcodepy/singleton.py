"""
# @author chrisxu
# @create 2020-09-26 13:38
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""
from functools import wraps


def Singleton(cls):
    _instance = {}

    @wraps(cls)
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton
