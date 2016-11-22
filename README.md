# A Blog with the Flask
This is a Blog that use Flask build,and use Markdown to write articles.I use it to build my blog [Kimxu's Blog](https://kimxu.herokuapp.com/)


# How to use it ?

1. download it form github.
2. makesure your python version going to python3.
`$ virtualenv --python=/usr/bin/python3 yourenv $ source bin/activate` 

3. cd the folder run the cmd `pip install -r requirements.txt`
4. set the `manage.py` `new_user()  u = User(email='kimxu_me@163.com', username='kimxu',password='12345678', confirmed=True)`
use a account by yourself
5. run the cmd `python manage.py new_user`
6. run the cmd `python manage.py runserver`
7. if you want to upload article that is a markdown file(.md) 
    1.login your account  `/users/login` login
    2.upload your article in `index.html` in the lower right corner

your markdown article like this :

```
title: 关于本博客
summary:博客介绍 
authors: Kimxu
publish_date: 2016-11-22
categories: 关于
tags: 关于

# 关于博客

本博客是本人（Kimxu）开发的一个基于Markdown的博客系统，后端采用Python的Flask系统，
前端采用Bootstrap、AngularJs(以后会用采用Cordova技术，开发IOS、Android版本)。
博客会开源出来，也算是为开源世界贡献出一点力。
```

After the upload,the system will change the md file to Html file,that can auto sort out.



