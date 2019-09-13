# -*- coding: utf-8 -* -
"""
函数注解器的使用
"""

def spamrun(fn):
    def sayspam(*args):
        print("spam,spam,spam")
        fn(*args)
    return sayspam

# 相当于spamrun(useful)(2,5)
@spamrun
def useful(a,b):
    print(a*b)

'''
打印：
spam,spam,spam
10
'''
useful(2,5)

def pre1(fn):
    def do_pre1(*args):
        print("pre1,pre1,pre1")
        fn(*args)
    return do_pre1

def pre2(fn):
    def do_pre2(*args):
        print("pre2,pre2,pre2")
        fn(*args)
    return do_pre2

#  相当于 pre2(pre1(post))(name)
@pre1
@pre2
def post(name):
    print("hello " + name)

'''
打印：
pre1,pre1,pre1
pre2,pre2,pre2
hello rensike 
'''
post("rensike")


# ======== 带参数的调用 ==========
def attrs(**kwargs):
    def decorate(f):
        for k in kwargs:
            setattr(f,k,kwargs[k])
        return f
    return decorate

@attrs(version=2.2,author="leilei")
def mymethod(num):
    print(getattr(mymethod,"version",0))
    print(getattr(mymethod,"author",""))
    print(num)

'''
打印：
2.2
leilei
9
'''
mymethod(9)









