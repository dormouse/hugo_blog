---
title: "pandas 入门"
date: 2015-02-07 10:26:33
lastmod: 2015-03-10 13:55:57
tags: ["pandas","matplot"]
categories: ["development"]
slug: "pandas-note"
---

建立环境
--------

### 安装 pandas

    sudo apt-get install build-essential python-dev
    sudo apt-get install python-pandas python-tk
    sudo apt-get install python-scipy python-matplotlib python-tables
    sudo apt-get install python-numexpr python-xlrd python-statsmodels
    sudo apt-get install python-openpyxl python-xlwt python-bs4

### 安装 ipython-notebook

    sudo pip install "ipython[notebook]"
    sudo pip install pygments

### 运行 ipython-notebook

    ipython notebook
    #如果你使用matplotlib内嵌进网页中,那么需要运行:
    ipython notebook --matplotlib inline

导入 pandas
-----------

    import pandas as pd
    import numpy as np

读入数据
--------

    # 读入 CSV 格式数据
    # 数据来源：http://boxofficemojo.com/daily/
    df_movies = pd.read_csv('movies.csv', sep='\t', encoding='utf-8')
    df_movies.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> $26,168,351</td>
      <td> American Sniper</td>
      <td>  $9,905,616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> $41,633,588</td>
      <td> American Sniper</td>
      <td> $16,510,536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> $12,515,579</td>
      <td> American Sniper</td>
      <td>  $4,244,376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  $6,475,068</td>
      <td> American Sniper</td>
      <td>  $2,645,109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  $7,825,091</td>
      <td> American Sniper</td>
      <td>  $2,923,141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    df_movies = pd.read_csv('movies.csv', sep='\t', encoding='utf-8',thousands=',',escapechar='$')
    df_movies.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

复制数据
--------

    df = df_movies.copy()
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

导出数据
--------

    #导出周六的数据，格式为 CSV
    df[ (df['Day'] == 'Sat') ].to_csv('test_output.csv', mode='w', encoding='utf-8', index=False)

    #在前面的文件中追加周日的数据
    df[ (df['Day'] == 'Sun') ].to_csv('test_output.csv', mode='a', header=False, encoding='utf-8', index=False)

显示数据
--------

    #显示开头的数据，缺省显示 5 条
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    #显示开头的数据，指定显示 3 条
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

    #显示末尾的数据，缺省显示 5 条
    df.tail()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td> 25</td>
      <td> Feb. 23</td>
      <td> Mon</td>
      <td> 54</td>
      <td>  7385671</td>
      <td> Fifty Shades of Grey</td>
      <td> 1846390</td>
    </tr>
    <tr>
      <th>25</th>
      <td> 26</td>
      <td> Feb. 24</td>
      <td> Tue</td>
      <td> 55</td>
      <td>  9424126</td>
      <td> Fifty Shades of Grey</td>
      <td> 2265910</td>
    </tr>
    <tr>
      <th>26</th>
      <td> 27</td>
      <td> Feb. 25</td>
      <td> Wed</td>
      <td> 56</td>
      <td>  6862942</td>
      <td> Fifty Shades of Grey</td>
      <td> 1772230</td>
    </tr>
    <tr>
      <th>27</th>
      <td> 28</td>
      <td> Feb. 26</td>
      <td> Thu</td>
      <td> 57</td>
      <td>  7161773</td>
      <td> Fifty Shades of Grey</td>
      <td> 1790520</td>
    </tr>
    <tr>
      <th>28</th>
      <td> 29</td>
      <td> Feb. 27</td>
      <td> Fri</td>
      <td> 58</td>
      <td> 26457000</td>
      <td>         Focus (2015)</td>
      <td> 6465000</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    #显示末尾的数据，缺省显示 2 条
    df.tail(2)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>27</th>
      <td> 28</td>
      <td> Feb. 26</td>
      <td> Thu</td>
      <td> 57</td>
      <td>  7161773</td>
      <td> Fifty Shades of Grey</td>
      <td> 1790520</td>
    </tr>
    <tr>
      <th>28</th>
      <td> 29</td>
      <td> Feb. 27</td>
      <td> Fri</td>
      <td> 58</td>
      <td> 26457000</td>
      <td>         Focus (2015)</td>
      <td> 6465000</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 7 columns</p>
</div>

    #只显示指定的行和列
    df.iloc[[1,3,5],[0,1,2,3]]

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
    </tr>
    <tr>
      <th>5</th>
      <td> 6</td>
      <td>  Feb. 4</td>
      <td> Wed</td>
      <td> 35</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 4 columns</p>
</div>

    df.loc[[1,3,5],['Date', 'Gross']]

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td> Jan. 31</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>3</th>
      <td>  Feb. 2</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>5</th>
      <td>  Feb. 4</td>
      <td>  2273342</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 2 columns</p>
</div>

操作单元
--------

    df = df_movies.copy()
    # 单元格赋值
    # 单个单元格赋值
    df.ix[0, u'#1 Movie'] = u'土豆之歌'
    df.loc[df.index[1], u'Gross']= 999
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td>            土豆之歌</td>
      <td> 9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td>     999</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td> 4244376</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

    # 多单个单元格赋值
    df.loc[df.index[0:2], u'Gross'] = [100, 200]
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td>            土豆之歌</td>
      <td>     100</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td>     200</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td> 4244376</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

操作列
------

### 改变列头

#### 使用 columns 属性

    df = df_movies.copy()
    #用一个列表来显式地指定，列表长度必须与列数一致
    # 示例 1
    df.columns = [u'row', u'date', u'weekday', u'day', u'top10gross', u'no1moive', u'gross']
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>row</th>
      <th>date</th>
      <th>weekday</th>
      <th>day</th>
      <th>top10gross</th>
      <th>no1moive</th>
      <th>gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> jan. 30</td>
      <td> fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> american sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    # 示例 2 ：大写转小写
    df.columns = [c.lower() for c in df.columns]
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>row</th>
      <th>date</th>
      <th>weekday</th>
      <th>day</th>
      <th>top10gross</th>
      <th>no1moive</th>
      <th>gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

#### 使用 rename 方法

    # 示例 1 ：小写转大写
    df = df.rename(columns=lambda x: x.upper())
    df.tail(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ROW</th>
      <th>DATE</th>
      <th>WEEKDAY</th>
      <th>DAY</th>
      <th>TOP10GROSS</th>
      <th>NO1MOIVE</th>
      <th>GROSS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26</th>
      <td> 27</td>
      <td> Feb. 25</td>
      <td> Wed</td>
      <td> 56</td>
      <td>  6862942</td>
      <td> Fifty Shades of Grey</td>
      <td> 1772230</td>
    </tr>
    <tr>
      <th>27</th>
      <td> 28</td>
      <td> Feb. 26</td>
      <td> Thu</td>
      <td> 57</td>
      <td>  7161773</td>
      <td> Fifty Shades of Grey</td>
      <td> 1790520</td>
    </tr>
    <tr>
      <th>28</th>
      <td> 29</td>
      <td> Feb. 27</td>
      <td> Fri</td>
      <td> 58</td>
      <td> 26457000</td>
      <td>         Focus (2015)</td>
      <td> 6465000</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

    # 示例 2 ：改变特定的列头
    df = df.rename(columns={'DATE': u'日期', 'GROSS': u'票房'})
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ROW</th>
      <th>日期</th>
      <th>WEEKDAY</th>
      <th>DAY</th>
      <th>TOP10GROSS</th>
      <th>NO1MOIVE</th>
      <th>票房</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

### 打印列类型

    df.columns.to_series().groupby(df.dtypes).groups

    # 打印列类型(清晰打印中文)
    types = df.columns.to_series().groupby(df.dtypes).groups
    for key, value in types.items():
        print key,':\t', ','.join(value)

### 插入列

    df = df_movies.copy()
    # 方式一：在末尾添加
    df['memo'] = pd.Series('', index=df.index)
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
      <th>memo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
      <td> </td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
      <td> </td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
      <td> </td>
    </tr>
  </tbody>
</table>
<p>3 rows × 8 columns</p>
</div>

    # 方式二：在中间插入
    df = df_movies.copy()
    df.insert(loc=1, column=u'year', value=u'2015')
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>year</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> 2015</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> 2015</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td> 2015</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 8 columns</p>
</div>

    # 根据现有值生成一个新的列
    df = df_movies.copy()
    df.insert(loc = 5 , column=u'OtherGross', value=df[u'Top 10 Gross'] - df[u'Gross'])
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>OtherGross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> 16262735</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> 25123052</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td>  8271203</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 8 columns</p>
</div>

    # 根据现有值生成多个新的列
    # 方法一
    df = df_movies.copy()
    def process_date_col(text):
        #根据日期生成月份和日两个新的列
        if pd.isnull(text):
            month = day = np.nan
        else:
            month, day = text.split('.')
        return pd.Series([month, day])

    df[[u'month', u'day']] = df.Date.apply(process_date_col)
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
      <th>month</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
      <td> Jan</td>
      <td>  30</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
      <td> Jan</td>
      <td>  31</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
      <td> Feb</td>
      <td>   1</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
      <td> Feb</td>
      <td>   2</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
      <td> Feb</td>
      <td>   3</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 9 columns</p>
</div>

    # 方法二(结果同上，但是没有方法一好)
    df = df_movies.copy()
    for idx, row in df.iterrows():
        df.ix[idx, u'month'], df.ix[idx, 'day'] = process_date_col(row[u'Date'])
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
      <th>month</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
      <td> Jan</td>
      <td>  30</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
      <td> Jan</td>
      <td>  31</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
      <td> Feb</td>
      <td>   1</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
      <td> Feb</td>
      <td>   2</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
      <td> Feb</td>
      <td>   3</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 9 columns</p>
</div>

### 改变列值

    df = df_movies.copy()
    #根据一列的值改变另一列
    df[u'#1 Movie'] = df[u'#1 Movie'].apply(lambda x: x[::-1])
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> repinS naciremA</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> repinS naciremA</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> repinS naciremA</td>
      <td>  4244376</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

    # 同时改变多个列的值
    cols = [u'Gross', u'Top 10 Gross']
    df[cols] = df[cols].applymap(lambda x: x/10000)
    df.head(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 2616</td>
      <td> repinS naciremA</td>
      <td>  990</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 4163</td>
      <td> repinS naciremA</td>
      <td> 1651</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 1251</td>
      <td> repinS naciremA</td>
      <td>  424</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

操作行
------

    df = df_movies.copy()
    # 添加一个空行
    df = df.append(pd.Series(
                    [np.nan]*len(df.columns), # Fill cells with NaNs
                    index=df.columns),
                    ignore_index=True)
    df.tail(3)

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>27</th>
      <td> 28</td>
      <td> Feb. 26</td>
      <td> Thu</td>
      <td> 57</td>
      <td>  7161773</td>
      <td> Fifty Shades of Grey</td>
      <td> 1790520</td>
    </tr>
    <tr>
      <th>28</th>
      <td> 29</td>
      <td> Feb. 27</td>
      <td> Fri</td>
      <td> 58</td>
      <td> 26457000</td>
      <td>         Focus (2015)</td>
      <td> 6465000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>NaN</td>
      <td>     NaN</td>
      <td> NaN</td>
      <td>NaN</td>
      <td>      NaN</td>
      <td>                  NaN</td>
      <td>     NaN</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 7 columns</p>
</div>

空值处理（NaN）
---------------

    # 计数有空值的行
    nans = df.shape[0] - df.dropna().shape[0]
    print(u'一共有 %d 行出现空值' % nans)

    # 填充空值为`无`
    df.fillna(value=u'无', inplace=True)
    df.tail()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25</th>
      <td> 26</td>
      <td> Feb. 24</td>
      <td> Tue</td>
      <td> 55</td>
      <td>    9424126</td>
      <td> Fifty Shades of Grey</td>
      <td> 2265910</td>
    </tr>
    <tr>
      <th>26</th>
      <td> 27</td>
      <td> Feb. 25</td>
      <td> Wed</td>
      <td> 56</td>
      <td>    6862942</td>
      <td> Fifty Shades of Grey</td>
      <td> 1772230</td>
    </tr>
    <tr>
      <th>27</th>
      <td> 28</td>
      <td> Feb. 26</td>
      <td> Thu</td>
      <td> 57</td>
      <td>    7161773</td>
      <td> Fifty Shades of Grey</td>
      <td> 1790520</td>
    </tr>
    <tr>
      <th>28</th>
      <td> 29</td>
      <td> Feb. 27</td>
      <td> Fri</td>
      <td> 58</td>
      <td> 2.6457e+07</td>
      <td>         Focus (2015)</td>
      <td> 6465000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>  无</td>
      <td>       无</td>
      <td>   无</td>
      <td>  无</td>
      <td>          无</td>
      <td>                    无</td>
      <td>       无</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

排序
----

    df = df_movies.copy()
    # 添加一个空行
    df = df.append(pd.Series(
                    [np.nan]*len(df.columns), # Fill cells with NaNs
                    index=df.columns),
                    ignore_index=True)
    # 根据某一列排序（由低到高）
    df.sort(u'Gross', ascending=True, inplace=True)
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td> 13</td>
      <td> Feb. 11</td>
      <td> Wed</td>
      <td> 42</td>
      <td> 6138013</td>
      <td>      American Sniper</td>
      <td> 1468160</td>
    </tr>
    <tr>
      <th>13</th>
      <td> 14</td>
      <td> Feb. 12</td>
      <td> Thu</td>
      <td> 43</td>
      <td> 5969515</td>
      <td>            SpongeBob</td>
      <td> 1527552</td>
    </tr>
    <tr>
      <th>26</th>
      <td> 27</td>
      <td> Feb. 25</td>
      <td> Wed</td>
      <td> 56</td>
      <td> 6862942</td>
      <td> Fifty Shades of Grey</td>
      <td> 1772230</td>
    </tr>
    <tr>
      <th>27</th>
      <td> 28</td>
      <td> Feb. 26</td>
      <td> Thu</td>
      <td> 57</td>
      <td> 7161773</td>
      <td> Fifty Shades of Grey</td>
      <td> 1790520</td>
    </tr>
    <tr>
      <th>24</th>
      <td> 25</td>
      <td> Feb. 23</td>
      <td> Mon</td>
      <td> 54</td>
      <td> 7385671</td>
      <td> Fifty Shades of Grey</td>
      <td> 1846390</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    # 排序后重新编制索引
    df.index = range(1,len(df.index)+1)
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td> 13</td>
      <td> Feb. 11</td>
      <td> Wed</td>
      <td> 42</td>
      <td> 6138013</td>
      <td>      American Sniper</td>
      <td> 1468160</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 14</td>
      <td> Feb. 12</td>
      <td> Thu</td>
      <td> 43</td>
      <td> 5969515</td>
      <td>            SpongeBob</td>
      <td> 1527552</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 27</td>
      <td> Feb. 25</td>
      <td> Wed</td>
      <td> 56</td>
      <td> 6862942</td>
      <td> Fifty Shades of Grey</td>
      <td> 1772230</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 28</td>
      <td> Feb. 26</td>
      <td> Thu</td>
      <td> 57</td>
      <td> 7161773</td>
      <td> Fifty Shades of Grey</td>
      <td> 1790520</td>
    </tr>
    <tr>
      <th>5</th>
      <td> 25</td>
      <td> Feb. 23</td>
      <td> Mon</td>
      <td> 54</td>
      <td> 7385671</td>
      <td> Fifty Shades of Grey</td>
      <td> 1846390</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

过滤
----

    df = df_movies.copy()
    # 根据列类型过滤
    # 只选择字符串型的列
    df.loc[:, (df.dtypes == np.dtype('O')).values].head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>#1 Movie</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> American Sniper</td>
    </tr>
    <tr>
      <th>1</th>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> American Sniper</td>
    </tr>
    <tr>
      <th>2</th>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> American Sniper</td>
    </tr>
    <tr>
      <th>3</th>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> American Sniper</td>
    </tr>
    <tr>
      <th>4</th>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> American Sniper</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 3 columns</p>
</div>

    # 选择 artifact 为空值的行
    df.ix[0, u'Gross'] = np.nan
    df.ix[3, u'Gross'] = np.nan
    df[df[u'Gross'].isnull()].head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 7 columns</p>
</div>

    # 选择'Gross'为非空值的行
    df[df[u'Gross'].notnull()].head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
    <tr>
      <th>5</th>
      <td> 6</td>
      <td>  Feb. 4</td>
      <td> Wed</td>
      <td> 35</td>
      <td>  5819529</td>
      <td> American Sniper</td>
      <td>  2273342</td>
    </tr>
    <tr>
      <th>6</th>
      <td> 7</td>
      <td>  Feb. 5</td>
      <td> Thu</td>
      <td> 36</td>
      <td>  6165344</td>
      <td> American Sniper</td>
      <td>  2506106</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    # 根据条件过滤
    df[ (df[u'Day'] == u'Sat') | (df[u'Day#'] <= 32) ]

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 </th>
      <td>  1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td>      American Sniper</td>
      <td>      NaN</td>
    </tr>
    <tr>
      <th>1 </th>
      <td>  2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td>      American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2 </th>
      <td>  3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td>      American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>8 </th>
      <td>  9</td>
      <td>  Feb. 7</td>
      <td> Sat</td>
      <td> 38</td>
      <td> 59153298</td>
      <td>            SpongeBob</td>
      <td> 24086968</td>
    </tr>
    <tr>
      <th>15</th>
      <td> 16</td>
      <td> Feb. 14</td>
      <td> Sat</td>
      <td> 45</td>
      <td> 87900659</td>
      <td> Fifty Shades of Grey</td>
      <td> 36752460</td>
    </tr>
    <tr>
      <th>22</th>
      <td> 23</td>
      <td> Feb. 21</td>
      <td> Sat</td>
      <td> 52</td>
      <td> 43708356</td>
      <td> Fifty Shades of Grey</td>
      <td>  8991100</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 7 columns</p>
</div>

    df[ (df[u'Day'] == u'Sat') & (df[u'Day#'] <= 32) ]

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 7 columns</p>
</div>

切片
----

合并
----

统计：计数，平均，最大，最小，方差，标准差
------------------------------------------

同比，环比
----------

图形化
------

    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()

![pandas\_67\_1.png](/images/pandas_67_1.png)

    df = df_movies.copy()
    df[u'Date'] = pd.to_datetime(df[u'Date'] + ',2015' )
    df.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td>2015-01-30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td>2015-01-31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>2015-02-01</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>2015-02-02</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>2015-02-03</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    df.plot(x='Date', y=['Top 10 Gross', 'Gross'])

![pandas\_69\_1.png](/images/pandas_69_1.png)

使用另一个 DataFrame 来更新数据
-------------------------------

    df_1 = df_movies.copy()
    df_2 = pd.DataFrame({u'#1 Movie':[u'American Sniper',
                                u'SpongeBob',
                                u'Fifty Shades of Grey'],
                                u'chs':[u'美国阻击手',
                                        u'海绵宝宝',
                                        u'五十度灰']})
    df_1.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 7 columns</p>
</div>

    df_2.head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#1 Movie</th>
      <th>chs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>      American Sniper</td>
      <td> 美国阻击手</td>
    </tr>
    <tr>
      <th>1</th>
      <td>            SpongeBob</td>
      <td>  海绵宝宝</td>
    </tr>
    <tr>
      <th>2</th>
      <td> Fifty Shades of Grey</td>
      <td>  五十度灰</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 2 columns</p>
</div>

    pd.merge(df_1, df_2, on=u'#1 Movie').head()

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Date</th>
      <th>Day</th>
      <th>Day#</th>
      <th>Top 10 Gross</th>
      <th>#1 Movie</th>
      <th>Gross</th>
      <th>chs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
      <td> Jan. 30</td>
      <td> Fri</td>
      <td> 30</td>
      <td> 26168351</td>
      <td> American Sniper</td>
      <td>  9905616</td>
      <td> 美国阻击手</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 2</td>
      <td> Jan. 31</td>
      <td> Sat</td>
      <td> 31</td>
      <td> 41633588</td>
      <td> American Sniper</td>
      <td> 16510536</td>
      <td> 美国阻击手</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 3</td>
      <td>  Feb. 1</td>
      <td> Sun</td>
      <td> 32</td>
      <td> 12515579</td>
      <td> American Sniper</td>
      <td>  4244376</td>
      <td> 美国阻击手</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4</td>
      <td>  Feb. 2</td>
      <td> Mon</td>
      <td> 33</td>
      <td>  6475068</td>
      <td> American Sniper</td>
      <td>  2645109</td>
      <td> 美国阻击手</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 5</td>
      <td>  Feb. 3</td>
      <td> Tue</td>
      <td> 34</td>
      <td>  7825091</td>
      <td> American Sniper</td>
      <td>  2923141</td>
      <td> 美国阻击手</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 8 columns</p>
</div>

