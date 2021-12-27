import pymysql


def sql(sql,*args):

    '''
    :param sql:  "INSERT INTO users (key1, key2,...) VALUES (%s, %s,...)"
    :param args: 传入需要的字段信息
    :return: sql 返回值
    example: sql("INSERT INTO users (key1, key2) VALUES (%s, %s)",value1,value2)
    '''
    try:
        connection = pymysql.connect(host='39.107.79.10',
                                     user='root',
                                     password='123456',
                                     database='test',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    except BaseException:
        print('数据库连接失败')

    try:
        cur = connection.cursor()
        cur.execute(sql, args)
        connection.commit()
        result = cur.fetchall()
        return result
    except BaseException :
        return  False
    finally:
        connection.close()