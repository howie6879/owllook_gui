#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/6.
"""

import aiohttp
import asyncio
import async_timeout

from bs4 import BeautifulSoup
from urllib.parse import urlparse

from owllook_gui.utils import get_random_user_agent
from owllook_gui.spider.base_novels import BaseNovels


class BaiduNovels(BaseNovels):

    def __init__(self):
        super(BaiduNovels, self).__init__()

    async def data_extraction(self, html):
        """
        小说信息抓取函数
        :return:
        """
        try:
            url = html.select('h3.t a')[0].get('href', None)
            real_url = await self.get_real_url(url=url) if url else None
            if real_url:
                real_str_url = str(real_url)
                netloc = urlparse(real_str_url).netloc
                if netloc in self.latest_rules.keys():
                    if "http://" + netloc + "/" == real_str_url:
                        return None
                    if 'baidu' in real_str_url or netloc in self.black_domain:
                        return None
                    title = html.select('h3.t a')[0].get_text()
                    return {
                        'title': title,
                        'url': real_str_url.replace('index.html', ''),
                        'netloc': netloc
                    }
                else:
                    return None
            else:
                return None
        except Exception as e:
            return None

    async def get_real_url(self, url):
        """
        获取百度搜索结果真实url
        :param url:
        :return:
        """
        with async_timeout.timeout(5):
            async with aiohttp.ClientSession() as client:
                try:
                    headers = {'user-agent': await get_random_user_agent()}
                    async with client.head(url, headers=headers, allow_redirects=True) as response:
                        self.logger.info('Parse url: {}'.format(response.url))
                        url = response.url if response.url else None
                        return url
                except Exception as e:
                    self.logger.error('获取URL: {} 失败'.format(url))
                    return None

    async def novels_search(self, novels_name):
        """
        小说搜索入口函数
        :return:
        """
        url = self.config.URL_PC
        params = {'wd': novels_name, 'ie': 'utf-8', 'rn': self.config.BAIDU_RN, 'vf_bl': 1}
        headers = {'user-agent': await get_random_user_agent()}
        html = await self.fetch_url(url=url, params=params, headers=headers)
        if html:
            soup = BeautifulSoup(html, 'html5lib')
            result = soup.find_all(class_='result')
            extra_tasks = [self.data_extraction(html=i) for i in result]
            tasks = [asyncio.ensure_future(i) for i in extra_tasks]
            done_list, pending_list = await asyncio.wait(tasks)
            res = [task.result() for task in done_list if task.result()]
            return res
        else:
            return []


async def start(novels_name):
    """
    Start spider
    :return:
    """
    return await BaiduNovels.start(novels_name)


if __name__ == '__main__':
    # Start
    res = asyncio.get_event_loop().run_until_complete(start('intitle:雪中悍刀行 小说 阅读'))
    print(res)
