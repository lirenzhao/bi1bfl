#!/usr/bin/python3
 
import pymysql

config = {
    'host':'rm-bp1h033d8uzmntj18.mysql.rds.aliyuncs.com',#4>8
    'port':3306,
    'db_user':'r2gl0a3x22',
    'db_pwd':'123@gooaocN',
    'db':'r2gl0a3x22',
    'encoding':'utf8'
}

def getConnection():
    return pymysql.connect(host=config['host'],
                           port=config['port'],
                           user=config["db_user"],
                           password=config["db_pwd"],
                           database=config["db"],
                           charset=config["encoding"])

def getVersion():
    try:
        db = getConnection()
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print ("Database version : %s " % data)
    finally:
        cursor.close()
        db.close()

def insert(table_name,data):
    db = getConnection()
    cur = db.cursor()

    sql = "INSERT INTO {} ({}) VALUES ({})"
    col = ""
    val = ""

    for k in data:
        col = col + k +","
        if type('a') == type(data[k]):
            val = val + "'"+ data[k] +"',"
        if type(1) == type(data[k]):
            val = val + ""+ str(data[k]) +","

    sql = sql.format(table_name,col[:-1],val[:-1])
    print(sql)

    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        cur.close()
        db.close()
db = None
cur = None
def insert2(table_name,data):
    global db
    global cur

    if not db:
        db = getConnection()
        cur = db.cursor()

    sql = "INSERT INTO {} ({}) VALUES ({})"
    col = ""
    val = ""

    for k in data:
        col = col + k +","
        if type('a') == type(data[k]):
            val = val + "'"+ data[k] +"',"
        if type(1) == type(data[k]):
            val = val + ""+ str(data[k]) +","

    sql = sql.format(table_name,col[:-1],val[:-1])
    print(sql)
    try:
        cur.execute(sql)
    except Exception as e:
        print(e)

def insert2_commit():
    global db
    global cur
    try:
        print("commit")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def insert2_close():
    global db
    global cur
    try:
        cur.close()
        db.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    data = {
        'font':'赵',
        'cate':'行书',
        'title':'来自篆刻字典',
        'images':'./images/赵/行书/02.jpg',
    }
    ret = insert('shufa_font',data)
    print(ret)