if __name__ == '__main__':
    x = 'Hello world!'
    print("x=",x)

    print("x[0]=",x[0])
    print("x[1]=",x[1])

    """Hello
        Hello
        Hello
        !
        !
    """
    print("x[0:5:1]=",x[0:5:1])
    print("x[0:5]=",x[0:5])
    print("x[:5]=",x[:5])
    print("x[-1]=",x[-1:])
    print("x[-1:]=",x[-1:])

    """world
    world
    """
    print("x[-6:-1]=",x[-6:-1])
    print("x[6:11]=",x[6:11])

    """world!
    """
    print("x[-6:]=",x[-6:])

    """
    world!
    world!
    !ldrow ooleH
    Hlowrd
    """
    print("x[6:]=",x[6:])
    print("x[6:12]=",x[6:12])
    print("x[::-1]=",x[::-1])
    print("x[::2]=",x[::2])