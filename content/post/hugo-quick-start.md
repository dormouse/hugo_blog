---
title: "Hugo Quick Start"
date: 2017-01-18 21:12:42
lastmod: 2017-01-18 21:12:42
tags: ["hugo"]
categories: ["software"]
slug: "hugo-quick-start"
description: "Hugo is a static site generator. This post will build a blog with"
---


    Hugo quickly.

What is Hugo?
-------------

Hugo is a general-purpose website framework. Technically speaking, Hugo
is a static site generator.

Website: <https://gohugo.io/>

DOC: <https://gohugo.io/overview/introduction/>

Quick start
-----------

### Install

#### Linux

    sudo apt-get install hugo

OR

Download the appropriate version for your platform from \[Hugo
Releases\]( <https://github.com/gohugoio/hugo/releases>)

Put it in `/usr/local/bin`

#### MacOS

    $ brew update && brew install hugo

Check Hugo

    $ hugo help
    $ hugo version

### Install Pygments

    $ sudo apt-get install python-pygments

Start new site

    $ hugo new site hugo_blog

Get theme

    $ cd hugo_blog/themes
    $ git clone https://github.com/dim0627/hugo_theme_robust.git

More theme at <http://themes.gohugo.io/>

Start new post

    $ cd ..
    $ hugo new post/hugo-quick-start.md

Start Server

    $ hugo server --theme=hugo_theme_robust --buildDrafts

Undragt post

    $ hugo undraft content/post/good-to-great.md

Continuous deployment
---------------------

Create package.json like follow:

``` {.sourceCode .json}
{
  "_aerobatic": {
    "build": {
      "engine": "hugo",
      "themeRepo": "https://github.com/alexurquhart/hugo-geo.git"
    }
  }
}
```

Push to Bitbucket

    # initialize new git repository
    git init

    # add /public directory to our .gitignore file
    echo "/public" >> .gitignore

    # commit and push code to master branch
    git add -A
    git commit -m "Init"
    git remote add origin ssh:git@bitbucket.org:YourUsername/your-hugo-site.git
    git push -u origin master

front matter
------------

The front matter is one of the features that gives Hugo its strength. It
enables you to include the meta data of the content right with it. Hugo
supports a few different formats, each with their own identifying
tokens.

TOML Example

    +++
    title = "spf13-vim 3.0 release and new website"
    description = "spf13-vim is a cross platform distribution of vim plugins and resources for Vim."
    tags = [ ".vimrc", "plugins", "spf13-vim", "vim" ]
    date = "2012-04-06"
    categories = [
      "Development",
      "VIM"
    ]
    slug = "spf13-vim-3-0-release-and-new-website"
    +++

    Content of the file goes Here

### Variables

There are a few predefined variables that Hugo is aware of and utilizes.
The user can also create any variable they want. These will be placed
into the `.Params` variable available to the templates. Field names are
always normalized to lowercase (e.g. camelCase: true is available as
`.Params.camelcase` ).

### Required variables

-   *title* The title for the content
-   *description* The description for the content
-   *date* The date the content will be sorted by
-   *taxonomies* These will use the field name of the plural form of the
    index (see tags and categories above)

### Optional variables

-   *aliases* An array of one or more aliases (e.g. old published path
    of a renamed content) that would be created to redirect to this
    content. See [Aliases](https://gohugo.io/extras/aliases/) for
    details.
-   *draft* If true, the content will not be rendered unless `hugo` is
    called with `--buildDrafts`
-   *publishdate* If in the future, content will not be rendered unless
    `hugo` is called with `--buildFuture`
-   *expirydate* Content already expired will not be rendered unless
    `hugo` is called with `--buildExpired`
-   *type* The type of the content (will be derived from the directory
    automatically if unset)
-   *isCJKLanguage* If true, explicitly treat the content as CJKLanguage
    (`.Summary` and `.WordCount` can work properly in CJKLanguage)
-   *weight* Used for sorting
-   *markup* (Experimental) Specify `"rst"` for reStructuredText
    (requires `rst2html`) or `"md"` (default) for Markdown
-   *slug* appears as tail of the url. It can be used to change the part
    of the url that is based on the filename.
-   *url* The full path to the content from the web root. It makes no
    assumptions about the path of the content file. It also ignores any
    language prefixes of the multilingual feature.

If neither `slug` or `url` is present, the filename will be used.

## Refence

-   [Hugo Quickstart Guide](https://gohugo.io/overview/quickstart/)
-   [Hugo chinese doc](http://www.gohugo.org/)
-   [Continuous deployment with Bitbucket &
    Aerobatic](https://gohugo.io/tutorials/hosting-on-bitbucket/)

