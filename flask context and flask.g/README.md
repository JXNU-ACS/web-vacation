## flask context
#### 一 . app context
上下文，如：
>他原来住在这

其中的‘他’你需要联系上下文来知道是指谁。
app context其实就是一个对象,指的就是当前的app。

flask中current_app就是一种app context。
其实app context是要被创建的。我们常用flask-scripts来为我们隐式创建而不是显式创建。

app context 用栈flask._app_ctx_stack 来存储。

#### 二 . request context
同样用栈来存储，所以当没有请求时去访问request下的属性会报错，因为此时的存储它的栈为空.
此外，request是建立在一个app上的。
[flask context 学习资料](https://blog.tonyseek.com/post/the-context-mechanism-of-flask/)
#### 二 . flask g
在flask __version__ >0.9中，g已经是app context而不是request context.虽然说g是和app绑定在一起的，但不同请求的AppContext是不同的，所以g还是不同。也就是说你不能再一个视图中设置g.name，然后再另一个视图中使用g.name，会提示AttributeError.这就是和session的区别。

g.在普通网站通常用于数据库的连接断开 [这是例子](http://dormousehole.readthedocs.io/en/latest/patterns/sqlite3.html)；在restful服务中主要用于保存某一次请求所需要的信息