if __name__ == '__main__':
    x=(12,"abc",3.45)
    print("x=",x)

    x=("abc",[1,'def'],3.45,(2,'ghi'))
    print("x=",x)

    print("x[0]=",x[0])
    print("x[3]=",x[3])
    print("x[3][1]=",x[3][1])

    print("x[0:3]=",x[0:3])

    """如果元组内包含可变对象，则可变对象的内容可以被改变"""
    x[1][0] = 45
    print("x=",x)

    print('abc' in x)
    print([45,'def'] not in x)


    y=("jk",15)
    print("y=",y)
    print(x+y) #此行编译器给出告警？
