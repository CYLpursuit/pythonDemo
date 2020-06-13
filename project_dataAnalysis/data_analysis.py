import pandas as pd
import matplotlib.pyplot as plt
import pylab as mpl #并没有再次加载模块，而是在matplotlib.pylab内含有
import getJSON

data = getJSON.getJson()
# 读取JSON文件
filepath = 'C:/Users/Administrator/Desktop/python/project_dataAnalysis/data.json'
df = pd.read_json(filepath)# 含有中文字符 必须指定字符集
# 查看df信息
# df.info()
length = len(df['deviceInfo'])
# 列表list（可变 类似数组） 元组、字符串
x = []
y1 = []
y2 = []
y3 = []
for i in range(length):
    itemX = df['deviceInfo'].iloc[i]
    itemY1 = df['trainTicket'].iloc[i]
    itemY2 = df['fightTicket'].iloc[i]
    itemY3 = df['busTicket'].iloc[i]
    x.append(itemX)
    y1.append(itemY1)
    y2.append(itemY2)
    y3.append(itemY3)
plt.figure()
mpl.rcParams['font.sans-serif']=['SimHei']
# plt.subplot(221)
title = plt.title('折线图',fontsize=14,color='gray')#标题
xlabel = plt.xlabel('机型',fontsize=12,color='gray')#轴标题
ylabel = plt.ylabel('时间',fontsize=12,color='gray')
plt.plot(x,y1,color='red',label='火车票')#作图
plt.plot(x,y2,color='green',label='飞机票')
plt.plot(x,y3,label='汽车票')
plt.legend()#图例
plt.show()#绘图