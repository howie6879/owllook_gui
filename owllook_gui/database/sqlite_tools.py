#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/11.
"""

from owllook_gui.config import Config
from owllook_gui.spider import get_latest_chapter


async def sql_delete_item(table_ins, engine, values: dict):
    async with engine.connect() as conn:
        await conn.execute(table_ins.delete(table_ins.c.url == values['url']))
        Config.LOGGER.info('书籍删除成功{}：{}'.format(values['title'], values['url']))


async def sql_insert_item(table_ins, engine, values: dict):
    async with engine.connect() as conn:
        latest_chapter_name, latest_chapter_url = await get_latest_chapter(values.get('url'))
        values.update({
            'latest_chapter_name': latest_chapter_name,
            'latest_chapter_url': latest_chapter_url,
        })
        await conn.execute(table_ins.insert().values(values))
        Config.LOGGER.info('书籍插入成功{}：{}'.format(latest_chapter_name, latest_chapter_url))


async def sql_get_all_result(table_name, engine):
    async with engine.connect() as conn:
        sql_res = await conn.execute('select * from {}'.format(table_name))
        result = await sql_res.fetchall()
        Config.LOGGER.info('书籍获取成功')
        return result
