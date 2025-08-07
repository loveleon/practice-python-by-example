if __name__=="__main__":
    s = set("textbook")
    print("s=",s)

    t = frozenset(["notebook"])
    print("t=",t)

    """成员操作符可用集合，判断元素是否为集合成员"""
    print("t" in s)
    print("o" not in s)

    """添加与删除只能用于可变集合， 添加一个元素，把in当成了一个元素"""
    s.add("in")
    print("s=",s)

    """添加多个元素，把in当成了两个元素，一个是i，一个是n"""
    s.update("in")
    print("s=",s)

    """删除集合中的一个元素"""
    s.remove("in")
    print("s=",s)

    """删除多个元素(使用求差集的方法), 删除元素i与元素n"""
    s -= set("in")
    print("s=",s)

    """判断子集使用小于符号(<, <=)"""
    print(set('book') < set('bocket'))
    print(set('bocket') <= set('bocket'))

    """判断超集使用大于符号(>, >=)"""
    print(set('bocket') > set('book'))
    print(set('bocket') >= set('bocket'))

    """"""
    print(set("book") | set("bike"))
    print(set("book") & set("bike"))
    print(set("book") - set("bike"))
    print(set("book") ^ set("bike"))


