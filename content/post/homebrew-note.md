---
title: "Homebrew Note"
date: 2017-02-05 22:34:28
lastmod: 2017-02-08 13:13:57
tags: ["homebrew","note"]
categories: ["software"]
slug: "homebrew-note"
description: "Note for homebrew."
---



Office site: <http://brew.sh/> .

Install
-------

Just Paste follow at a Terminal prompt:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Usage
-----

Example:

    $ brew install wget

What is it?

Homebrew installs packages to their own directory and then symlinks
their files into /usr/local:

    $ cd /usr/local
    $ find Cellar
    Cellar/wget/1.16.1
    Cellar/wget/1.16.1/bin/wget
    Cellar/wget/1.16.1/share/man/man1/wget.1

    $ ls -l bin
    bin/wget -> ../Cellar/wget/1.16.1/bin/wget

Homebrew-Cask
-------------

Homebrew-Cask extends Homebrew and brings its elegance, simplicity, and
speed to the installation and management of GUI macOS applications such
as Google Chrome and Adium.

We do this by providing a friendly Homebrew-style CLI workflow for the
administration of macOS applications distributed as binaries.

It’s implemented as a homebrew external command called cask.

To start using Homebrew-Cask, you just need Homebrew installed.

Example:

    $ brew cask install atom
    ==> Satisfying dependencies
    complete
    ==> Downloading https://github.com/atom/atom/releases/download/v1.8.0/atom-mac.zip
    ######################################################################## 100.0%
    ==> Verifying checksum for Cask atom
    ==> Moving App 'Atom.app' to '/Applications/Atom.app'
    ==> Symlinking Binary 'apm' to '/usr/local/bin/apm'
    ==> Symlinking Binary 'atom.sh' to '/usr/local/bin/atom'
    🍺  atom was successfully installed!

And there we have it. Atom installed with one quick command: no
clicking, no dragging, no dropping.
