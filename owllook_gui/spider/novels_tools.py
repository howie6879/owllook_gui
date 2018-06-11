#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/11.
"""

import aiohttp

import async_timeout

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from owllook_gui.config import Config
from owllook_gui.utils import get_random_user_agent


async def get_latest_chapter(chapter_url):
    headers = {
        'user-agent': await get_random_user_agent()
    }
    latest_chapter_name, latest_chapter_url = '', ''
    netloc = urlparse(chapter_url).netloc

    if netloc in Config.LATEST_RULES.keys():
        html = await fetch_url(url=chapter_url, params=None, headers=headers)
        if html:
            try:
                soup = BeautifulSoup(html, 'html5lib')
            except Exception as e:
                Config.LOGGER.exception(e)
                return latest_chapter_name, latest_chapter_url

            if Config.LATEST_RULES[netloc].plan:
                meta_value = Config.LATEST_RULES[netloc].meta_value
                latest_chapter_name = soup.select(
                    'meta[property="{0}"]'.format(meta_value["latest_chapter_name"])) or soup.select(
                    'meta[name="{0}"]'.format(meta_value["latest_chapter_name"]))

                latest_chapter_name = latest_chapter_name[0].get('content',
                                                                 None) if latest_chapter_name else None
                latest_chapter_url = soup.select(
                    'meta[property="{0}"]'.format(meta_value["latest_chapter_url"])) or soup.select(
                    'meta[name="{0}"]'.format(meta_value["latest_chapter_url"]))
                latest_chapter_url = urljoin(chapter_url, latest_chapter_url[0].get('content',
                                                                                    None)) if latest_chapter_url else None
    return latest_chapter_name, latest_chapter_url


async def fetch_url(url, params, headers):
    """
    公共抓取函数
    :param url:
    :param params:
    :return:
    """
    with async_timeout.timeout(10):
        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(url, params=params, headers=headers) as response:
                    assert response.status == 200
                    Config.LOGGER.info('Task url: {}'.format(response.url))
                    try:
                        text = await response.text()
                    except:
                        text = await response.read()
                    return text
        except Exception as e:
            Config.LOGGER.exception(e)
            return None
