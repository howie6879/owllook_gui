#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/6.
"""
import asyncio

from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse

from owllook_gui.utils import get_random_user_agent
from owllook_gui.spider.base_novels import BaseNovels


class SoNovels(BaseNovels):

    def __init__(self):
        super(SoNovels, self).__init__()

    async def data_extraction(self, html):
        """
        小说信息抓取函数
        :return:
        """
        try:
            # 2017.09.09 修改 更加全面地获取title && url
            try:
                title = html.select('h3 a')[0].get_text()
                url = html.select('h3 a')[0].get('href', None)
            except Exception as e:
                self.logger.exception(e)
                return None

            # 针对不同的请进行url的提取
            if "www.so.com/link?m=" in url:
                url = html.select('h3 a')[0].get('data-url', None)
            if "www.so.com/link?url=" in url:
                url = parse_qs(urlparse(url).query).get('url', None)
                url = url[0] if url else None

            netloc = urlparse(url).netloc
            # print(url)
            # print(netloc)

            if netloc in self.latest_rules.keys():
                if str(url).endswith(netloc + '/'):
                    return None
                if not url or 'baidu' in url or 'baike.so.com' in url or '.html' in url or netloc in self.black_domain:
                    return None
                return {
                    'title': title,
                    'url': url.replace('index.html', '').replace('Index.html', ''),
                    'netloc': netloc
                }
            else:
                return None
        except Exception as e:
            self.logger.exception(e)
            return None

    async def novels_search(self, novels_name):
        """
        小说搜索入口函数
        :return:
        """
        url = self.config.SO_URL

        headers = {
            'User-Agent': await get_random_user_agent(),
            'Referer': "http://www.so.com/haosou.html?src=home"
        }
        params = {'ie': 'utf-8', 'src': 'noscript_home', 'shb': 1, 'q': novels_name, }
        html = await self.fetch_url(url=url, params=params, headers=headers)
        if html:
            soup = BeautifulSoup(html, 'html5lib')
            result = soup.find_all(class_='res-list')
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
    return await SoNovels.start(novels_name)


if __name__ == '__main__':
    # Start
    res = asyncio.get_event_loop().run_until_complete(start('雪中悍刀行 小说 最新章节'))
    print(res)
