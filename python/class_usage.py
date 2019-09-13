# -*- coding: utf-8 -* -
"""
python 魔法方法
"""

class Hello():
    def __init__(self):
        print("Hello Class")

    def test_inherit(self,name):
        print("I love " + name)


class World(Hello):
    def __init__(self):
        super(World,self).__init__()

    def test_inherit(self,name):
        super(World,self).test_inherit(name)

    @property
    def name(self):
        return "rensike"

    def __call__(self, *args, **kwargs):
        print("多余参数 args:",args)
        print("关键字传值 kwargs:",kwargs)

    def __str__(self):
        return self.__class__.__name__


class Students():
    def __init__(self,*args):
        self.names = args
        self.i = 0

    def __len__(self):
        return len(self.names)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self):
            raise StopIteration
        item = self.names[self.i % len(self)]
        self.i += 1
        return item


if __name__ == '__main__':
    my_word = World()
    my_word.test_inherit("leilei")
    my_word(1,3,"hello",name="rsk",conmany="baidu")
    print(my_word.name)
    print(my_word)

    my_students = Students("xiaoming","xiaohong","xiaobao","xiaohua")
    print(len(my_students))
    for student in my_students:
        print("student name = ",student)
