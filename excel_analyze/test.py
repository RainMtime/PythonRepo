# -*- coding: UTF-8 -*-
# 测试想DataFrame中添加一行

import openpyxl
import pandas as pd

if __name__ == "__main__":
    ddf = pd.DataFrame([[1, 3, 4]], columns=['语文', 'b', 'c'])
    sum = 0
    ap = pd.DataFrame([[sum, 3, 5]], columns=['语文', 'b', 'c'])
    ddf = ddf.append(ap, ignore_index=True)
    ddf.to_excel("result.xlsx", "Sheet4")
    print ddf
