from pymongo import MongoClient


if __name__ == '__main__':
    print("Hello !")
    conn = MongoClient('mongodb://127.0.0.1:27017')
    db = conn.mydb #连接mydb数据库，没有则自动创建
    my_set = db.poly #使用test_set集合，没有则自动创建
    #my_set.insert({"name":"zhangsan","age":18})
    # for i in my_set.find():
    #     print(i)
    # #查询name=zhangsan的
    # for i in my_set.find({"name":"zhangsan"}):
    #     print(i)
    # print(my_set.find_one({"name":"zhangsan"}))