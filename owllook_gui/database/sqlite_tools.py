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


async def sql_get_all_result(table_name, engine):
    async with engine.connect() as conn:
        sql_res = await conn.execute('select * from {}'.format(table_name))
        result = await sql_res.fetchall()
        Config.LOGGER.info('书籍获取成功')
        return result


async def sql_insert_item(table_ins, engine, values: dict):
    async with engine.connect() as conn:
        latest_chapter_name, latest_chapter_url = await get_latest_chapter(values.get('url'))
        values.update({
            'latest_chapter_name': latest_chapter_name,
            'latest_chapter_url': latest_chapter_url,
        })
        await conn.execute(table_ins.insert().values(values))
        Config.LOGGER.info('书籍插入成功{}：{}'.format(latest_chapter_name, latest_chapter_url))


async def sql_update_item(table, engine, condition: dict, values: dict):
    async with engine.connect() as conn:
        await conn.execute(
            "update {table} set latest_chapter_name='{latest_chapter_name}',  latest_chapter_url='{latest_chapter_url}' where  title='{title}' and url='{url}' ".format(
                table=table,
                latest_chapter_name=values['latest_chapter_name'],
                latest_chapter_url=values['latest_chapter_url'],
                title=condition['title'],
                url=condition['url']
            ))

        Config.LOGGER.info('{}：{}更新成功'.format(condition['title'], condition['url']))
