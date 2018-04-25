# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

import datetime

import matplotlib.pyplot as plt
from matplotlib import style

#   s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

if __name__ == "__main__":
    print ("hello_MaTian")
    style.use('fivethirtyeight')
    df = pd.read_excel('all_data.xlsx', 'Sheet2')
    # df = pd.DataFrame([[1, 2, 3, 4], [1, 6, 3, 8],[2,3,3,4]], columns=['学校', "高管", "s", "for"])
    # 输出表信息
    print df.info()
    # 输出表头
    print df.head(3)
    # 输出表尾
    print df.tail(3)

    # test = pd.DataFrame([[1, 2, 3, 4], [1, 6, 3, 8], [2, 3, 3, 4]], columns=['学校', "高管", "s", "for"])
    #
    # for iterItem in test.iterrows():
    #     print iterItem
    # 去重
    # print df.drop_duplicates("学校")
    # 每个公司每年高管的总数
    # 每个公司每年女性高管的总数
    # 每个公司每年所有高管的平均年龄



    companyList = df.drop_duplicates('company')['company']

    datetimeList = df.drop_duplicates('date')['date']
    resultPd = pd.DataFrame(
        columns=['company', '2008', '2008-women', '2008-average', '2009', '2009-women', '2009-average', '2010',
                 '2010-women', '2010-average', '2011', '2011-women',
                 '2011-average', '2012', '2012-women', '2012-average',
                 '2013',
                 '2013-women', '2013-average', '2014', '2014-women', '2014-average', '2015', '2015-women',
                 '2015-average', '2016', '2016-women', '2016-average'])
    # 循环遍历，输出分析结果：
    for item in companyList:
        dict = {'company': 0, '2008': 0, '2008-women': 0, '2008-average': 0, '2009': 0, '2009-women': 0,
                '2009-average': 0, '2010': 0,
                '2010-women': 0, '2010-average': 0, '2011': 0, '2011-women': 0,
                '2011-average': 0, '2012': 0, '2012-women': 0, '2012-average': 0,
                '2013': 0,
                '2013-women': 0, '2013-average': 0, '2014': 0, '2014-women': 0, '2014-average': 0, '2015': 0,
                '2015-women': 0,
                '2015-average': 0, '2016': 0, '2016-women': 0, '2016-average': 0}
        dict['company'] = item
        for datetimeItem in datetimeList:
            manCount = 0
            womenCount = 0
            allage = 0
            realDf = df[(df.company == item) & (df.date == datetimeItem)]
            for rowItem in realDf.itertuples(index=True, name='Pandas'):
                if getattr(rowItem, "gender") == u'男':
                    manCount = manCount + 1
                    allage = allage + getattr(rowItem, "age")
                else:
                    womenCount = womenCount + 1
                    allage = allage + getattr(rowItem, "age")
            # 存储到字典里面
            dict[datetimeItem[0:4]] = manCount + womenCount
            dict[datetimeItem[0:4] + "-women"] = womenCount
            if manCount + womenCount == 0:
                continue
            dict[datetimeItem[0:4] + "-average"] = allage / (manCount + womenCount)

        tempPd = pd.DataFrame([[item, dict.get('2008'), dict.get('2008-women'), dict.get('2008-average'),
                                dict.get('2009'), dict.get('2009-women'), dict.get('2009-average'),
                                dict.get('2010'), dict.get('2010-women'), dict.get('2010-average'),
                                dict.get('2011'), dict.get('2011-women'), dict.get('2011-average'),
                                dict.get('2012'), dict.get('2012-women'), dict.get('2012-average'),
                                dict.get('2013'), dict.get('2013-women'), dict.get('2013-average'),
                                dict.get('2014'), dict.get('2014-women'), dict.get('2014-average'),
                                dict.get('2015'), dict.get('2015-women'), dict.get('2015-average'),
                                dict.get('2016'), dict.get('2016-women'), dict.get('2016-average')]],
                              columns=['company', '2008', '2008-women', '2008-average', '2009',
                                       '2009-women', '2009-average', '2010',
                                       '2010-women', '2010-average', '2011', '2011-women',
                                       '2011-average', '2012', '2012-women', '2012-average',
                                       '2013',
                                       '2013-women', '2013-average', '2014', '2014-women',
                                       '2014-average', '2015', '2015-women',
                                       '2015-average', '2016', '2016-women',
                                       '2016-average'])  # print ("%s  %s  %d   %d  %d" % (item, datetimeItem, manCount, womenCount, manCount + womenCount))
        resultPd = resultPd.append(tempPd, ignore_index=True)
resultPd.to_excel("result.xlsx", "Sheet3")
