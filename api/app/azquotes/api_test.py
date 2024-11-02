# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: api_test.py
# @Author: sunbcy
# @Institution: SYLG University, LiaoNing, China
# @E-mail: saintbcy@163.com
# @Time: 10月 23, 2024 22:56
# ---
import aiohttp
import asyncio
from lxml import etree


class AsyncQuotesBot:
    """异步获取azquotes
    """
    def __init__(self):
        self.quote_main_url = "https://azquotes.com"
        self.quote_main_url_headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }

    async def fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.quote_main_url, headers=self.quote_main_url_headers) as response:
                return await response.text()

    async def get_today_quote(self):
        try:
            r = await self.fetch()
            html = etree.HTML(r)
            quote_today = html.xpath('//div[@class="content-slide content-slide_top"]/p/a[@class="title"]/text()')
            quote_author_today = html.xpath(
              '//div[@class="content-slide content-slide_top"]/div[@class="q_user"]/a/text()')
            print("今日Quotes获取成功!")
            quotes = dict(zip(quote_author_today, quote_today))
            return quotes
        except Exception as e:
            print("今日Quotes获取失败!")
            return


async def main():
    client = AsyncQuotesBot()
    r = await client.get_today_quote()
    print(r)


# Python 3.7 及以上版本可以直接这样运行
if __name__ == '__main__':
    asyncio.run(main())
