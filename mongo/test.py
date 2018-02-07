from pymongo import MongoClient
import datetime
import time
import random

if __name__ == '__main__':
    print("Hello !")
    conn = MongoClient('mongodb://127.0.0.1:27017')
    db = conn.logs
    logs_set = db.login_log

    # login_log = []    
    # for i in range(1,100):
    #     d = {}
    #     d['user_id'] = i
    #     d['User_name'] = 'user_' + str(i)
    #     d['login_date'] = datetime.datetime.now()
    #     d['terminal_no'] = int(100 * random.random())
    #     time.sleep(2 * random.random())
    #     print(d)
    #     login_log.append(d)
    # ret = logs_set.insert_many(login_log)
    # print(ret)

    l = logs_set.find_one({'user_id':2})
    print(type(l))
    for i in l:
        print(i,':',l[i])