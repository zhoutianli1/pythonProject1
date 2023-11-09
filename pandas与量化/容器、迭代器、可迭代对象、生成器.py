'''
，容器就是存储某些元素的统称
在 Python 中，我们通常使用 in 或 not in 来判断一个元素存在/不存在于一个容器
str、list、tuple、set、dict 都可以通过 in 或 not in 来判断一个元素是否在存在/不存在这个实例中，所以这些类型我们都可以称作「容器」。
这是因为它们都实现了 __contains__ 方法。
'''
class A:

    def __init__(self):
        self.items = [1, 2]

    def __contains__(self, item):
        return item in self.items
a = A()
print(1 in a)   # True
print(3 in a)   # False
'''
我们在开发时，除了使用 in 判断元素是否在容器内之外，另外一个常用的功能是：输出容器内的所有元素。
例如执行 for x in [1, 2, 3]，就可以迭代出容器内的所有元素。
一个类如果实现了「迭代器协议」，就可以称之为「迭代器」。
在 Python 中，实现迭代器协议就是实现以下 2 个方法：

__iter__：这个方法返回对象本身，即 self
__next__：这个方法每次返回迭代的值，在没有可迭代元素时，抛出 StopIteration 异常
下面我们来看一个实现迭代器协议的例子：

'''
class AA:
    """A 实现了迭代器协议 它的实例就是一个迭代器"""
    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()

# 迭代元素
a = AA(3)
for i in a:
    print(i)
# 再次迭代 没有元素输出 因为迭代器只能迭代一次
for i in a:
    print(i)
'''
，容器就是存储某些元素的统称

'''

'''
，容器就是存储某些元素的统称

'''