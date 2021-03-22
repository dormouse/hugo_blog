---
title: "Sphinx cheat sheet"
date: 2013-09-10
tags: ["sphinx"]
categories: ["software"]
slug: "sphinx-cheet-sheet"
---

Here is a quick and dirty cheat sheet for some common stuff you want to
do in sphinx and ReST.

文本格式化
----------

  名称 |代码      |示例
  -----|------    |-----------------------
  斜体 |`*斜体* ` |*斜体*
  粗休 |`**粗体**`|**粗体**
  原文 |\`原文\`  |`原文`

源代码
------

末尾使用 `::` 符号，则下面的内容就显示为源代码,源代码需要缩进，例如:

    You can represent code blocks fairly easily::

       import numpy as np
       x = np.random.rand(12)

以上代码显示效果如下：

    You can represent code blocks fairly easily:

        import numpy as np
        x = np.random.rand(12)

也可以直接从文件引入代码。例如从exts/chinese\_search.py
引入代码可以使用如下命令:

    .. literalinclude:: exts/chinese_search.py

生成列表
--------

+------------------------+---------------------+
| 代码                   | 显示效果            |
+========================+=====================+
| `* point A`            | -   point A         |
|                        | -   point B         |
| `* point B`            | -   point C         |
|                        |                     |
| `* point C`            |                     |
+------------------------+---------------------+
| `#. point A`           | 1.  point A         |
|                        | 2.  point B         |
| `#. point B`           | 3.  point C         |
|                        |                     |
| `#. point C`           |                     |
+------------------------+---------------------+

制作表格
--------

复杂表格写法如下:

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      |          |
    +------------------------+------------+----------+----------+

简单表格写法如下:

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

制作链接
--------

`` `mysite <http://mysite.com>`_ `` 显示为 [mysite](http://mysite.com)
。

`http://www.mysite.com` 直接显示为 <http://www.mysite.com> 。

`` :ref:`making-a-table ``\` 用于引用文章内部章节。

`` :mod:`matplotlib.backend_bases ``\` 用于引用模块。

`` :class:`~matplotlib.backend_bases.LocationEvent ``\` 用于引用类。

`` :meth:`~matplotlib.backend_bases.FigureCanvasBase.mpl_connect ``\`
用于引用方法。

划分章节
--------

-   `#` with overline, for parts
-   `*` with overline, for chapters
-   `=`, for sections
-   `-`, for subsections
-   `^`, for subsubsections
-   `"`, for paragraphs

全局替换
--------

reST支持“替换”，例如:

    .. |name| replace:: replacement *text*

或者:

    .. |caution| image:: warning.png
                 :alt: Warning!

如果你想在所有文件使用中这些替换，一种方式是把它们写入 rst\_prolog ；
另一种方式是把它们放到一个单独的文件中，然后在需要使用的文件中使用:

    :rst:dir:`include`

指令来导入这些替换。

Sphinx 内置的全局替换有 `|today|` 、 `|release|` 和 `|version|` 。

today 表示当前日期（时间），其显示格式可以通过 conf.py 文件中的
today\_fmt 来设置。

图像
----

使用方法:

    .. image:: gnu.png
       (options)

When used within Sphinx, the file name given (here `gnu.png`) must
either be relative to the source file, or absolute which means that they
are relative to the top source directory. For example, the file
`sketch/spam.rst` could refer to the image `images/spam.png` as
`../images/spam.png` or `/images/spam.png`.

Sphinx will automatically copy image files over to a subdirectory of the
output directory on building (e.g. the `_static` directory for HTML
output.)

Interpretation of image size options (`width` and `height`) is as
follows: if the size has no unit or the unit is pixels, the given size
will only be respected for output channels that support pixels (i.e. not
in LaTeX output). Other units (like `pt` for points) will be used for
HTML and LaTeX output.

Sphinx extends the standard docutils behavior by allowing an asterisk
for the extension:

    .. image:: gnu.*

Sphinx then searches for all images matching the provided pattern and
determines their type. Each builder then chooses the best image out of
these candidates. For instance, if the file name `gnu.*` was given and
two files gnu.pdf and gnu.png existed in the source tree, the LaTeX
builder would choose the former, while the HTML builder would prefer the
latter.

### 脚注

脚注用 `[#name]_` 来表示，在文档底部“ Footnotes ”标题后写具体内容:

    Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

    .. rubric:: Footnotes

    .. [#f1] Text of the first footnote.
    .. [#f2] Text of the second footnote.

You can also explicitly number the footnotes (`[1]_`) or use
auto-numbered footnotes without names (`[#]_`).

### Citations

Standard reST citations are supported, with the additional feature that
they are "global", i.e. all citations can be referenced from all files.
Use them like so:

    Lorem ipsum [Ref]_ dolor sit amet.

    .. [Ref] Book or article reference, URL or whatever.

Citation usage is similar to footnote usage, but with a label that is
not numeric or begins with `#`.

### Comments

Every explicit markup block which isn't a valid markup construct (like
the footnotes above) is regarded as a comment . For example:

    .. This is a comment.

You can indent text after a comment start to form multiline comments:

    ..
       This whole indented block
       is a comment.

       Still in the comment.

### Gotchas

There are some problems one commonly runs into while authoring reST
documents:

-   **Separation of inline markup:** As said above, inline markup spans
    must be separated from the surrounding text by non-word characters,
    you have to use a backslash-escaped space to get around that. See
    [the
    reference](http://docutils.sf.net/docs/ref/rst/restructuredtext.html#inline-markup)
    for the details.
-   **No nested inline markup:** Something like `` *see :func:`foo`* ``
    is not possible.

