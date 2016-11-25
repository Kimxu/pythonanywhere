title: 博客安装使用介绍
summary: 主要是介绍这个博客的安装和使用流程
authors: Kimxu
publish_date: 2016-11-25
categories: 技术
tags: 博客

> 良心文章啊~用了我的美好夜晚~TAT

# 前言
用了小半个月的时间，忙里偷闲的把博客搭建完成了。期间遇到了挺多坑，也想到放弃，想想一个做安
卓的，去做前端，做后端，也是挺不容易的。不过一咬牙坚持下来了。用了好多第三方速成的博客，
怎么感觉都不舒服，最后一狠心，做了个自己的博客。我的地盘我做主，以后想撒撒娇卖卖萌都可以了，
23333。一直都是用大神们开源的项目，所以这次自己也开源了这个博客源码，写的不好，轻喷啊，
希望可以得到大神的指导 [源码点我TAT](https://github.com/Kimxu/pythonanywhere)

#介绍
这个项目前端使用的Bootstrap+AngularJs，后端使用的Python（Python版本3.5）的Web框架Flask。
文章使用的是Markdown格式，可以直接写MD文章，之后传到博客上，博客会自动根据MD进行文章分类。
以后准备会出移动端，有这方面想法的小伙伴可以一起做啊~~~

# 安装
1. 从github上把项目拷贝下来，也可以直接使用 git命令 :
`git clone https://github.com/Kimxu/pythonanywhere.git`
2. 使用PyCharm打开项目，之后使用命令 pip install -r requirements.txt 把需要安装的依赖安装一下。
不出问题的话 这里在命令行运行 `python manage.py runserver` ,浏览器登录`http://127.0.0.1:5000`
不出意外的话会出现下图:
![](http://ww4.sinaimg.cn/large/006y8mN6gw1fa4q8bd2qhj30yo05cdh5.jpg){: class="img-responsive"}
3. 之后需要生成一个账号来登录网站后台进行文章上传，在命令行运行`python manage.py`生成一个测试账号
可以自己在`manage.py`文件中修改。账号：`kimxu_me@163.com`，密码：`123456`。
4. 浏览器输入`http://127.0.0.1:5000/users/login`
![](http://ww2.sinaimg.cn/large/006y8mN6gw1fa4qeekbz0j31kw0zk0un.jpg){: class="img-responsive"}
登录之后，在主页右下角会出现`上传MD`按钮，之后可以把写好的文章上传上去，后台就会自动的给文章进行分类排版

# 文章规定
文章开头使用
```
title: 这个是文章标题
summary: 这里是文章的简介
authors: 这里是作者名字
publish_date: 2016-11-25 （这里是发布时间）
categories: 技术 （这里是目录分类）
tags: 博客 （标签分类）
```


文章里面里面 使用
```
# 标题1
内容内容内容内容
## 小标题2
内容内容内容内容
### 小标题3
内容内容内容内容
```

之后会自动根据`#`生成目录
![](http://ww3.sinaimg.cn/large/006y8mN6gw1fa4spof0otj31kw0zkahf.jpg){: class="img-responsive"}


# MarkDown 语法

项目里面使用的是 [官方文档](https://pythonhosted.org/Markdown) 
Markdown的一些高级语法可以参考 [Markdown参数介绍](https://pythonhosted.org/Markdown/extensions/index.html)
可以在`generate.py`中进行设置。
``` Python
def render(md_file, site_id):
    """渲染html页面
    :param md_file:
    :return:
    """
    with codecs.open(md_file, "r", "utf-8") as f:
        text = f.read()
        md = Markdown(
            extensions=[
                "fenced_code",
                "attr_list",
                "codehilite(css_class=highlight,linenums=None)",
                "meta",
                "admonition",
                "tables",
                "toc",
                "wikilinks",
            ],
        )
        html = md.convert(text)
        meta = md.Meta if hasattr(md, "Meta") else {}
        toc = md.toc if hasattr(md, "toc") else ""
        create_index(md_file, meta)
        article_url = '/posts/' + site_id
        template = env.get_template("posts/article_base.html")
        text = template.render(
            blog_content=html,
            static_root=STATIC_ROOT,
            site_id=site_id,
            article_url=article_url,
            title=ARTICLE_INDEX[_current_file_index].get("title"),
            title_html=render_title_html(ARTICLE_INDEX[_current_file_index].get("title")),
            summary=ARTICLE_INDEX[_current_file_index].get("summary", ""),
            authors=render_authors_html(ARTICLE_INDEX[_current_file_index].get("authors")),
            tags=render_tags_html(ARTICLE_INDEX[_current_file_index].get("tags")),
            toc=toc,
        )

    return text


```


有什么不懂的可以文章下留言~



