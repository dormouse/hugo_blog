#!/usr/bin/env python3
import os
import re
import sys
import glob
import subprocess

"""
Created: 20171008
Modified: 20171009
Purpose: Covert my pelican blog to hugo blog
"""

def process_file(target_file):
    with open(target_file, 'r') as f:
        line = f.read()
        new_line = process_line(line)
    with open(target_file, 'w') as f:
        f.write(new_line)


def process_line(line):
    # deal with front matters
    keys = ['title', 'date', 'lastmod', 'tags', 'categories', 'slug', 'description']
    matters = {}

    patt = re.compile(r'.+\n=+', re.M|re.I)
    m_obj = patt.match(line)
    if m_obj:
        matters['title'] = '"{}"'.format(m_obj.group().split('\n')[0])
        line = patt.sub('', line, 1)

    patt = re.compile(r'\ndate\n\n:   .+\n', re.M|re.I)
    m_obj = patt.search(line)
    if m_obj:
        matters['date'] = m_obj.group().split('   ')[1].strip()
        line = patt.sub('', line, 1)

    patt = re.compile(r'\nmodified\n\n:   .+\n', re.M|re.I)
    m_obj = patt.search(line)
    if m_obj:
        matters['lastmod'] = m_obj.group().split('   ')[1].strip()
        line = patt.sub('', line, 1)

    patt = re.compile(r'\ntags\n\n:   .+\n', re.M|re.I)
    m_obj = patt.search(line)
    if m_obj:
        items = m_obj.group().split('   ')[1].split(',')
        items = [item.strip() for item in items]
        items = ','.join(['"{}"'.format(item) for item in items])
        matters['tags'] = '[{}]'.format(items)
        line = patt.sub('', line, 1)

    patt = re.compile(r'\ncategory\n\n:   .+\n', re.M|re.I)
    m_obj = patt.search(line)
    if m_obj:
        items = m_obj.group().split('   ')[1].split(',')
        items = [item.strip() for item in items]
        items = ','.join(['"{}"'.format(item) for item in items])
        matters['categories'] = '[{}]'.format(items)
        line = patt.sub('', line, 1)

    patt = re.compile(r'\nslug\n\n:   .+\n', re.M|re.I)
    m_obj = patt.search(line)
    if m_obj:
        matters['slug'] = '"{}"'.format(m_obj.group().split('   ')[1].strip())
        line = patt.sub('', line, 1)

    patt = re.compile(r'\nsummary\n\n:   .+\n', re.M|re.I)
    m_obj = patt.search(line)
    if m_obj:
        matters['description'] = '"{}"'.format(m_obj.group().split('   ')[1].strip())
        line = patt.sub('', line, 1)

    patt = re.compile(r'\nauthor\n\n:   .+\n', re.M|re.I)
    m_obj = patt.search(line)
    if m_obj:
        line = patt.sub('', line, 1)


    all_matters = ['{}: {}'.format(key, matters[key]) for key in keys if key in matters]
    all_matters = "---\n{}\n---\n\n".format('\n'.join(all_matters))
    return all_matters + line

def process(source_path, target_path):
    # use pandoc convert rst to md
    source_files = glob.glob(os.path.join(source_path, '*.rst'))
    source_short_files = [os.path.split(file)[1] for file in source_files]
    source_noext_files = [os.path.splitext(file)[0] for file in source_short_files]
    target_files = [os.path.join(target_path, file+'.md') for file in source_noext_files]
    pandoc_cmd_template = 'pandoc -f rst -t markdown  -o {} {}'
    zip_files = zip(target_files, source_files)

    pandoc_cmds = [pandoc_cmd_template.format(zip_file[0], zip_file[1]) for zip_file in zip_files]
    for cmd in pandoc_cmds:
        print(cmd)
        subprocess.Popen(cmd, shell=True)

    # test_files = ['/home/dormouse/project/hugo_blog/content/post/apt-cheat-sheet.md',]
    # map(process_file, target_files)
    for target_file in target_files:
        process_file(target_file)

def main():
    base_path = '/home/dormouse/project'
    source_base_path = os.path.join(base_path, 'blog2017/content/articles')
    target_base_path = os.path.join(base_path, 'hugo_blog/content')

    source = source_base_path
    target = os.path.join(target_base_path, 'post')
    process(source, target)


    for path in ['lego', 'personal', 'python-notes']:
        source = os.path.join(source_base_path, path)
        target = os.path.join(target_base_path, path)
        process(source, target)

def test():
    source_file = '/home/dormouse/project/hugo_blog/content/post/python-terminal-ide.md'
    with open(source_file, 'r') as f:
        line = f.read()
        new_line = process_line(line)
        print(new_line)


if __name__ == '__main__':
    main()
    # test()
