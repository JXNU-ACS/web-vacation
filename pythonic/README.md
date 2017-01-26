## pythonic：python最佳实践
什么是python的最佳实践？其实就是多多利用python的一些特有的函数和控制结构等特性来写代码。一种功能可以由很多不同的python代码实现，但是我们要学习的只是其中的最pythonic的。与其浪费时间在用不同方法的代码实现同一种功能，不如只学习使用最pythonic的。
##### 1. 哪些是最pythonic的
例如：  
```
d={'x':1,'y':2,'z':3}
for key in d:
    print key,d[key]
```
改成
```
for key,value in d.iteritems()
    print key,value
```
再如
```
index=0
string = [1,2,3,4,5,6,7,8]
for i in string:
    print index,i
    index+=1
```
改成
```
for index,i in enumerate(string):
    print index,i
```
有时候你觉得已经很pythonic了，但是依然不够
```
f=open(r'somefile.txt',r)
try:
    f.write('hello')
finally:
    f.close()
```
可以改成
```
with open(r'somefile.txt',r) as f:
    f.write('hello')
```
#### 2.为什么你会写得不pythonic
原因大致分一下几种
1. 已经有其他语言的基础，所以写的代码风格有自己学过语言的味道
2. python的学习不够深入，思考的少
3. 优秀的代码看的少等等
#### 3.为什么你要写得pythonic
1. 性能好
2. 潜在的bug少
#### 4.推荐阅读书籍
<<编写高质量代码：改善Python程序的91个建议>>
[点击进入下载](http://pan.baidu.com/share/link?shareid=4105123030&uk=3560438215&errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0)

    
