if __name__ == '__main__':
    x = [12,"abc",3.45]
    print("x=",x)

    x=[12,"abc",3.45,[6,'def']]
    print("x=",x)

    """使用下标访问"""
    print("x[0]=",x[0])
    print("x[3]=",x[3])
    print("x[3][1]=",x[3][1])

    """使用切片访问"""
    print("x[1:3]=",x[1:3])

    """更新列表中特定位置的值"""
    x[2] = 7.89
    print("x=",x)

    """添加新的值到列表尾部"""
    x.append(10)
    print("x=",x)
    x.append("gh")
    print("x=",x)

    x.insert(2,"hello")
    print("x=",x)

    """删除列表中某个位置值"""
    del x[3]
    print("x=",x)

    print('abc' in x)
    print([6,'def'] not in x)

    """成员操作符、连接操作符可用于列表"""
    y=["jk",15]
    print("y=",y)
    print(x+y)
