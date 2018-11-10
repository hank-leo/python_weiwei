# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="weiwei")
        cur=conn.cursor()
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]
            sql="insert into dangdang(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            #conn.query(sql)
            cur.execute(sql)
            conn.commit()
        conn.close()
        return item
