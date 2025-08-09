"""
每隔1秒输出一次“hello, world”，持续1小时

Author: 晚来风急
Version: 1.0
"""
import time

if __name__ == '__main__':
    """
    for i in range(5):
        print(i)
        time.sleep(1)
    """
    for i in range(1,5):
        print(i)
    print("-----")
    for i in range(1,5,2):
        print(i)
    print("-----")

    for i in range(5,0,-2):
        print(i)

    print("-----")

    for _ in range(5):
        print("hello")
        time.sleep(1)