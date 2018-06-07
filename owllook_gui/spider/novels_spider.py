#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/6.
"""

from importlib import import_module


async def get_novels_info(class_name, novels_name):
    novels_module = import_module(
        "owllook_gui.spider.{}_novels".format(class_name))
    # 获取对应渠道实例化对象
    novels_info = await novels_module.start(novels_name)
    return novels_info


if __name__ == '__main__':
    import asyncio

    res = asyncio.get_event_loop().run_until_complete(
        get_novels_info(class_name='baidu', novels_name='intitle:雪中悍刀行 小说 阅读'))
    print(res)
