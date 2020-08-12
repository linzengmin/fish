import sqlite3
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import  numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
def findPageJobList():  
    try: 
        con = sqlite3.connect('./static/sqlitedb/datas.db')
        cur = con.cursor()
        sql = "select * from fish "  
        cur.execute(sql)
        result = cur.fetchall()
    except Exception as e:
        print(e)
        print('查询失败')
    finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()     
    #print(result)
    return result
'''
1号鱼：全长43.5厘米，体长37厘米，体高6厘米，体宽5.5厘米，腹围15.2厘米。
2号鱼：全长42.5，体长36.5，体宽7，体高6，腹围15
'''
def delAll():
     result=0
    try:
        con = sqlite3.connect('./static/sqlitedb/datas.db')
        cur = con.cursor()
        sql = "delete * from fish " 
        cur.execute(sql,(fname,))
        con.commit()
        else:
            print('no such file:%s'%fname)  # 则返回文件不存在
        except Exception as e:
            print(e)
            print('查询失败')
        finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()     
        return result
if __name__ == "__main__":
    result=findPageJobList()
    print(result)
    rate=[]
    count=0
    '''
    for i,x in enumerate(result):
        if(i%2==0):
            count+=1
            temprate=int(x[4])/(x[7]*7)
            rate.append(temprate)
        else:
            count+=1
            temprate=int(x[4])/(x[7]*5.5)
            rate.append(temprate)
    
    for i,x in enumerate(result):
        if(i%2==0):
            count+=1
            temprate=x[5]/(x[8]*6)
            rate.append(temprate)
    
    a=[]
    b=[]
    c=[]
    for i,x in enumerate(result):
        if(i%2==0):
            count+=1
            a.append(x[3]/36.5)
            b.append(x[4]/7)
            c.append(x[5]/6)
        else:
            count+=1
            a.append(x[3]/37)
            b.append(x[4]/5.5)
    sumA=0
    sumB=0
    sumC=0
    for x in a:
        sumA+=x
    for x in b:
        sumB+=x
    for x in c:
        sumC+=x
    print(sumA/(count*1000))
    print(sumB/(count*1000))
    print(sumC*2/(count*304))
'''
'''
8.831319088168405
7.678107606679035
21.238095238095237
'''

    
    