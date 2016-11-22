# -*- coding:utf-8 -*-
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


class HighlighterRenderer():
    def blockcode(self, text, lang):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(text.strip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()

        return highlight(code=text, lexer=lexer, formatter=formatter)

    def table(self, content):
        return u'\n<table class="table table-bordered table-hover">{}</table>\n'.format(content.strip())


if __name__ == '__main__':
    hight = HighlighterRenderer()
    formatter = HtmlFormatter()
    highlight('''/# 关于本文

本博客是本人（Yan）开发的一个基于Markdown的博客系统，支持基本的Markdown语法及一些常用的扩展语法。本文将对本博客所支持的Markdown语法做介绍。

# Markdown基本语法

Markdown基本语法参见：
[https://daringfireball.net/projects/markdown/syntax](https://daringfireball.net/projects/markdown/syntax)

# 扩展的Markdown特殊语法''', "<a>", formatter)
