# # from app.qiyewechat.routes import QiYeWeChatBot
from traceback import print_exc

import aiohttp
from app.utils import check_proxy
from app.utils import responses as resp
from app.utils.responses import response_with
from fastapi import APIRouter
from lxml import etree

router = APIRouter()


def deliver_quotes_to_qiyeweixin(quotes):
    if not quotes:
        return 'Where there is a will, there is a way!'
    for i in quotes:
        print(" {quote}".format(quote=quotes.get(i)))
        quote_str = """【Quote of today】\n{quote}\n\n--{author}""".format(quote=quotes.get(i), author=i)
        # Bot_1 = QiYeWeChatBot()
        # quote_str = {
        #     'text': quote_str
        # }
        # Bot_1.send_text(quote_str)
        break
    return quote_str


# class QuotesCollector:
#     def __init__(self) -> None:
#         self.s = requests.Session()
#         self.quote_main_url = "https://www.azquotes.com"
#         self.quote_main_url_headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
#
#     def crawl_page(self, page=''):
#         r = self.s.get(page, headers=self.quote_main_url_headers, proxies=check_proxy())
#         r.encoding = r.apparent_encoding
#         return r.text
#
#     def get_today_quote(self):
#         try:
#             r = self.crawl_page(self.quote_main_url)
#             html = etree.HTML(r)
#             quote_today = html.xpath('//div[@class="content-slide content-slide_top"]/p/a[@class="title"]/text()')
#             quote_author_today = html.xpath(
#                 '//div[@class="content-slide content-slide_top"]/div[@class="q_user"]/a/text()')
#             print("今日Quotes获取成功!")
#             quotes = dict(zip(quote_author_today, quote_today))
#             return quotes
#         except:
#             print("今日Quotes获取失败!")
#             return
#
#     # def deliver_quotes_to_mail(self, quotes):
#     #     quote_list = []
#     #     for i in quotes:
#     #         quote_list.append({i: quotes.get(i)})
#     #     quote_choice = random.choice(quote_list)
#     #     print(quote_choice)
#     #     quote_str = """【Quote of today】<br>{quote}<br><br>--{author}""".format(
#     #         quote=quote_choice[list(quote_choice.keys())[0]], author=list(quote_choice.keys())[0])
#     #     mailsender = MailSender()
#     #     mailsender.sendMail('MacBot', ['saintbcy@163.com'], [], 'Daily Logs Of ' + time.strftime('%Y%m%d'), mailsender.content(quote_str), attachments=[])


class AsyncQuotesBot:
    def __init__(self, proxy=check_proxy()):
        self.quote_main_url = "https://azquotes.com"
        self.quote_main_url_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }
        self.proxy = proxy['http']

    async def fetch(self):
        connector = None
        if self.proxy:
          connector = aiohttp.TCPConnector(ssl=False)

        async with aiohttp.ClientSession() as session:
            async with session.get(self.quote_main_url, headers=self.quote_main_url_headers, proxy=self.proxy) as response:
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
            print_exc()
            print("今日Quotes获取失败!")
            return {}


# @azquotes_bp.route('/', methods=['GET'])  # 同步版本
# def get_today_azquote():  # 目前只能获取当天的数据
#     quote_bot = QuotesCollector()
#     quotes_dict = quote_bot.get_today_quote()
#     quote_str = deliver_quotes_to_qiyeweixin(quotes_dict)  # 企业微信发送格言
#     value = {'searchResults': quote_str}
#     return response_with(resp.SUCCESS_200, value=value)

client = AsyncQuotesBot()


@router.get('/')  # 异步版本
async def get_today_azquote():  # 目前只能获取当天的数据
    quotes_dict = await client.get_today_quote()
    # print(quotes_dict)
    if not quotes_dict:
        return 'Where there is a will, there is a way!'
    for i in quotes_dict:
        quote_str = """【Quote of today】\n{quote}\n\n--{author}""".format(quote=quotes_dict.get(i), author=i)
        print(quote_str)
        break
    value = {'searchResults': quote_str}
    return response_with(resp.SUCCESS_200, value=value)


# if __name__ == '__main__':
#     quote_bot = QuotesCollector()
#     quotes_dict = quote_bot.get_today_quote()
#     # quote_bot.deliver_quotes_to_qiyeweixin(quotes_dict)  # 企业微信发送格言
#     # quote_bot.deliver_quotes_to_mail(quotes_dict)  # 邮件发送格言
