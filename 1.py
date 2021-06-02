import requests
from lxml import etree
import xlwt

# content = requests.get('http://find.nlc.cn/search/doSearch?query=%E7%A2%B3%E6%8E%92%E6%94%BE&secQuery=&actualQuery=%E7%A2%B3%E6%8E%92%E6%94%BE%20mediatype%3A(0%20OR%201%20OR%202)%20&searchType=2&docType=%E5%9B%BE%E4%B9%A6&mediaTypes=0,1,2&isGroup=isGroup&targetFieldLog=%E5%85%A8%E9%83%A8%E5%AD%97%E6%AE%B5&orderBy=RELATIVE#query--%E7%A2%B3%E6%8E%92%E6%94%BE%7C%7CsecQuery--%7C%7CactualQuery--%E7%A2%B3%E6%8E%92%E6%94%BE%20mediatype%3A(0%20OR%201%20OR%202)%20%7C%7CpageNo--1').content
# html = etree.HTML(content)
# links = html.xpath('//div[@class="book_right"]/div/a/@id')
# print(links)
# detail_url = 'http://find.nlc.cn/search/showDocDetails?docId=-5009663326029668229&dataSource=ucs01&query=%E7%A2%B3%E6%8E%92%E6%94%BE'
# d_html = etree.HTML(requests.get(detail_url).content)
# d_content = d_html.xpath('//div[@class="zy_pp_val"]/text()')
# print(d_content)
# 创建一个workbook 设置编码
keyword = input("关键词：")
page = int(input("总页数："))
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')
# 书名、作者、出版社、出版时间、摘要、中图分类号、关键词
worksheet.write(0, 0, label='书名')
worksheet.write(0, 1, label='作者')
worksheet.write(0, 2, label='出版社')
worksheet.write(0, 3, label='出版时间')
worksheet.write(0, 4, label='摘要')
worksheet.write(0, 5, label='中图分类号')
worksheet.write(0, 6, label='关键词')
line = 1
for i in range(1, page + 1):
    data = {
        "query": keyword,
        "secQuery": '',
        "actualQuery": f"{keyword} mediatype:(0 OR 1 OR 2)",
        "pageNo": i,
        "orderBy": "RELATIVE",
        "queryField": '',
        "fldText": "全部检索字段",
        "isGroup": "isGroup",
        "showcount": 0,
        "docType": "图书",
        "targetField": '',
        "targetFieldLog": " 全部字段",
        "orginQuery": f"{keyword} mediatype:(0 OR 1 OR 2)",
        "searchType": 2
    }
    content = requests.post(url='http://find.nlc.cn/search/ajaxSearch', data=data).content
    content = str(content, encoding='utf-8')
    html = etree.HTML(content)
    ids = html.xpath('//div[@class="book_name"]/a/@id')

    cnt = 1
    for bid in ids:
        d_url = f'http://find.nlc.cn/search/showDocDetails?docId={bid}&dataSource=ucs01&query=%E7%A2%B3%E6%8E%92%E6%94%BE'
        d_html = etree.HTML(requests.get(d_url).content)
        book_name = d_html.xpath('//div[@class="book_name"]/text()')
        zuozhe = d_html.xpath('(//div[@class="book_item"])[2]/a/span/text()')
        chubanshe = d_html.xpath('(//div[@class="book_item"])[3]/a/span/text()')
        chubanshijian = d_html.xpath('((//div[@class="book_item"])[4]/span)[2]/text()')
        zhaiyao = d_html.xpath('//div[@class="zy_pp_val"]/text()')
        # fenleihao = d_html.xpath('((//div[@id="detail-info"]/div)[8]/span)[2]/text()')
        # guanjianci = d_html.xpath('((//div[@id="detail-info"]/div)[6]/span)[2]/text()')
        sss = d_html.xpath('(//div[@class="book_item"]/span[@class="book_val"])')
        for s in range(len(sss)):
            title = str((sss[s].xpath('./text()'))[0]).split(' ')[0].strip()
            if title == '分类':
                fenlei = sss[s].xpath('(../span)[2]/text()')
            if title == '关键词':
                guanjianci = sss[s].xpath('(../span)[2]/text()')
        # print(str(book_name[0]).strip())
        # print(str(zuozhe[0]).strip())
        # print(str(chubanshe[0]).strip())
        # print(str(chubanshijian[0]).strip())
        # print(str(zhaiyao[0]).strip())
        # print(str(fenlei[0]).strip())
        # print(str(guanjianci[0]).strip())
        a1 = str(book_name[0]).strip() if len(book_name) != 0 else ''
        a2 = str(zuozhe[0]).strip() if len(zuozhe) != 0 else ''
        a3 = str(chubanshe[0]).strip() if len(chubanshe) != 0 else ''
        a4 = str(chubanshijian[0]).strip() if len(chubanshijian) != 0 else ''
        a5 = str(zhaiyao[0]).strip() if len(zhaiyao) != 0 else ''
        a6 = str(fenlei[0]).strip() if len(fenlei) != 0 else ''
        a7 = str(guanjianci[0]).strip() if len(guanjianci) != 0 else ''

        worksheet.write(line, 0, label=a1)
        worksheet.write(line, 1, label=a2)
        worksheet.write(line, 2, label=a3)
        worksheet.write(line, 3, label=a4)
        worksheet.write(line, 4, label=a5)
        worksheet.write(line, 5, label=a6)
        worksheet.write(line, 6, label=a7)
        print(f'{i}-{line}')
        line += 1
workbook.save(f'{keyword}.xls')
print('Finish')
