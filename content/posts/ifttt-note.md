---
title: "Ifttt Note"
date: 2017-05-21
lastmod: 2017-05-21
tags: ["ifttt","note"]
categories: ["software"]
slug: "ifttt-note"
description: "some note about ifttt"
---



IFTTT Maker
-----------

A simple test:

    import os

    def test():
        """
        Test ifttt maker

        the command template is:
            curl -X POST -H "Content-Type:application/json" -d
            '{"value1":"第一个参数","value2":"第二个","value2":"第三个"}'
            'https://maker.ifttt.com/trigger/test/with/key/your_key'
        :param:
        :return:
        """
        key = 'csO7ZoutwPzCc_Your_key'
        arg1 = '第一'
        arg2 = '第二'
        arg3 = '一二三四五六七八九十'

        template = [
            'curl -X POST -H "Content-Type:application/json" -d ',
            "'{",
            '"value1":"{}","value2":"{}","value3":"{}"'.format(arg1,arg2,arg3),
            "}' ",
            'https://maker.ifttt.com/trigger/test/with/key/',
            key
        ]
        os.system(''.join(template))

    if __name__ == '__main__':
        test()
