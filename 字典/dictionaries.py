if __name__ == '__main__':
    x={}
    y=dict()
    print("x=",x)
    print("y=",y)

    x = {'a':'alpha', 'b':'beta', 'c':'gamma'}
    y = dict((['g','gama'],['d','delta']))
    print("x=",x)
    print("y=",y)

    x['e']  = 'epsilon'
    y['z'] = 'zeta'
    print("x=",x)
    print("y=",y)

    x['a'] = 'apple'
    y['g'] = 'google'
    print("x=",x)
    print("y=",y)

    del y['g']
    print("y=",y)

    y.clear()
    print("y=",y)

    del y

    print('a' in x)
    print('b' not in x)

    print("x.keys()=",x.keys())
    print("x.values()=",x.values())

    print("x['a']=",x.get('a'))
    print("x['d']=",x.get('d'))

    for key,value in x.items():
        print("key=%s,value=%s" % (key,value))
