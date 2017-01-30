循环import
-------
#### 什么是循环import
举个例子
a.py
```
from b import bway
def away():
    print '123'
```
b.py
```
from a import away
def bway():
    print '321'
```
这就是循环import
网上很多人谈到这方面问题时，理解得太浅显,摘自某篇博客的一段话:
>在a.py中导入b.b(),在导入b文件的时候，又要去导入a文件，a文件又要去导入b文件，这是一个死循环了，自然是不允许的

解释地浅显就不说了，首先python解释器并非因为它是一个死循环而报错，其次，python允许循环import,其实这两方面是相辅相成的。报错中指出的是sys.modules中要from 的module中的__dict__没有所要import的所以会报错指出import的函数不存在

要理解循环import 需要明白from .. import .. 机制
![](http://i.imgur.com/LkimUsB.png)
[学习资料](http://python.jobbole.com/84174/)
####  那如何避免？
1. 结构上优化
#### 如何正确利用？
1. 把import放到最后
2. 在函数里面import（python核心编程第二版12.8.5）