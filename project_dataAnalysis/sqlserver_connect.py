import pymssql

# 连接数据库
def connectSql():
    print("开始连接数据库...")
    global conn
    conn = pymssql.connect(
        host='(local)',
        user='cyl',
        password='sqlserver',
        database='test'
    )
    # 获取游标
    global cursor
    cursor = conn.cursor()
    print('数据库连接成功...')

def close():
    cursor.close()
    conn.commit()
    conn.close()

# sqlserver 2016 新特性
def selectJson():
    connectSql()
    sqlJson ="select * from data_RN1 FOR JSON PATH"
    cursor.execute(sqlJson)
    result = cursor.fetchall()
    close()
    return result
