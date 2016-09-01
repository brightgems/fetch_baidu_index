#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import traceback

from baidu_index.browser import BaiduBrowser
from baidu_index.utils.log import logger
from baidu_index import config
import itertools as it
import pandas as pd
import datetime

def main():
    logger.info(u'请确保你填写的账号密码能够成功登陆百度')
    # s = BaiduBrowser(cookie_json='{"name": "1"}')
    # cookie_json = s.cookie_json
    # s.close()
    s = BaiduBrowser()

    fp = open(config.keywords_task_file_path, 'r',encoding='utf8')
    kw_list = fp.readlines()
    fp.close()
    fp = open(config.cities_task_file_path, 'r',encoding='utf8')
    city_list = fp.readlines()
    fp.close()

    root = os.path.dirname(os.path.realpath(__file__))
    result_folder = os.path.realpath(config.out_file_path)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    type_list = config.index_type_list
    df_bdi = pd.DataFrame()
    for keyword,city in it.product(kw_list,city_list):
        try:
            keyword = keyword.strip()
            city = city.strip()
            if not keyword:
                continue
            
            baidu_index_list = s.get_baidu_index(keyword, city, type_list)
            df_one = pd.DataFrame(baidu_index_list)
            if df_bdi.empty:
                df_bdi = df_one
            else:
                df_bdi = df_bdi.append(df_one, ignore_index=True)

        except:
            print(traceback.format_exc())

    d = datetime.datetime.now()
    file_name = '%s.csv' % (d.strftime("%Y%m%d-%H%M%S"))
    file_path = os.path.join(result_folder, file_name)
    df_bdi.to_csv(file_path,index=False)


if __name__ == '__main__':
    main()