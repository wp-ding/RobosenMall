import pymysql

import sqlite3

# from RobosenMall.settings.common import BASE_DIR

# def createtb():
#     conn = sqlite3.connect('/code/RobosenMall/db.sqlite3')
#     print('数据库打开成功')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE COMPANY
#            (ID INT PRIMARY KEY     NOT NULL,
#            NAME           TEXT    NOT NULL,
#            AGE            INT     NOT NULL,
#            ADDRESS        CHAR(50),
#            SALARY         REAL);''')
#     print ("数据表创建成功")
#     conn.commit()
#     conn.close()

# def inserttb():
#     conn = sqlite3.connect('/code/RobosenMall/db.sqlite3')
#     c = conn.cursor()
#     print("数据库打开成功")
#
#     c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#           VALUES (1, 'Paul', 32, 'California', 20000.00 )")
#
#     c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#           VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
#
#     c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#           VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
#
#     c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#           VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
#
#     conn.commit()
#     print("数据插入成功")
#     conn.close()


# def selecttb():
#     conn = sqlite3.connect('/code/RobosenMall/db.sqlite3')
#     c = conn.cursor()
#     print("数据库打开成功")
#
#     cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
#     for row in cursor:
#        print("ID = ", row[0])
#        print("NAME = ", row[1])
#        print("ADDRESS = ", row[2])
#        print("SALARY = ", row[3], "\n")
#        print(type(row[3]))
#     print ("数据查询成功")
#     conn.close()

# def updatetb():
#     conn = sqlite3.connect('/code/RobosenMall/db.sqlite3')
#     c = conn.cursor()
#     print ("数据库打开成功")
#     c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
#     conn.commit()
#     print("Total number of rows updated :", conn.total_changes)
#
#     cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
#     for row in cursor:
#        print("ID = ", row[0])
#        print("NAME = ", row[1])
#        print("ADDRESS = ", row[2])
#        print("SALARY = ", row[3], "\n")
#     print("数据更新成功")
#     conn.close()

# def deletetb():
#     conn = sqlite3.connect('/code/RobosenMall/db.sqlite3')
#     c = conn.cursor()
#     print ("数据库打开成功")
#     c.execute("DELETE from COMPANY where ID=2;")
#     conn.commit()
#     print("Total number of rows deleted :", conn.total_changes)
#
#     cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
#     for row in cursor:
#        print("ID = ", row[0])
#        print("NAME = ", row[1])
#        print("ADDRESS = ", row[2])
#        print("SALARY = ", row[3], "\n")
#     print("数据删除成功")
#     conn.close()

# if __name__ == '__main__':
    # a = createtb()
    # b = inserttb()
    # c = selecttb()
    # d = updatetb()
    # e = deletetb()




# pymysql增删查改

# 创建数据库
# def mysql_ins():
#     db = pymysql.connect(host='localhost',
#                          user='root',
#                          password='password',
#                          database='robosen_project')
#
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#
#     # # 使用 execute() 方法执行 SQL，如果表存在则删除
#     # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
#     # 使用预处理语句创建表
#     sql = """CREATE TABLE EMPLOYEE (
#              FIRST_NAME  CHAR(20) NOT NULL,
#              LAST_NAME  CHAR(20),
#              AGE INT,
#              SEX CHAR(1),
#              INCOME FLOAT )"""
#
#     cursor.execute(sql)
#
#     # 关闭数据库连接
#     db.close()

# # 插入数据
# def mysql_ins():
#     db = pymysql.connect(host='localhost',
#                          user='root',
#                          password='password',
#                          database='robosen_project')
#
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#
#     # SQL 插入语句
#     sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#              LAST_NAME, AGE, SEX, INCOME)
#              VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#     # 插入语句的另一种写法
#     # sql = "INSERT INTO EMPLOYEE(FIRST_NAME,
#     #        LAST_NAME, AGE, SEX, INCOME)
#     #        VALUES ('%s', '%s',  %s,  '%s',  %s)" %
#     #       ('Mac', 'Mohan', 20, 'M', 2000)
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 如果发生错误则回滚
#         db.rollback()
#
#     # 关闭数据库连接
#     db.close()
#
# # 查询数据
# def mysql_sel():
#     db = pymysql.connect(host='localhost',
#                          user='root',
#                          password='password',
#                          database='robosen_project')
#
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#
#     # SQL 查询语句
#     sql = "SELECT * FROM EMPLOYEE \
#            WHERE INCOME > %s" % (1000)
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 获取所有记录列表
#         results = cursor.fetchall()
#         for row in results:
#             fname = row[0]
#             lname = row[1]
#             age = row[2]
#             sex = row[3]
#             income = row[4]
#             # 打印结果
#             print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#                   (fname, lname, age, sex, income))
#     except:
#         print("Error: unable to fetch data")
#
#     # 关闭数据库连接
# #     db.close()
#
# # 更新数据
# def mysql_upd():
#     db = pymysql.connect(host='localhost',
#                          user='root',
#                          password='password',
#                          database='robosen_project')
#
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#
#     # SQL 更新语句
#     sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 发生错误时回滚
#         db.rollback()
#
#     # 关闭数据库连接
#     db.close()
#
# # 删除数据
# def mysql_del():
#     db = pymysql.connect(host='localhost',
#                          user='root',
#                          password='password',
#                          database='robosen_project')
#
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # SQL 删除语句
#     sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 提交修改
#         db.commit()
#     except:
#         # 发生错误时回滚
#         db.rollback()
#
#     # 关闭连接
#     db.close()

# 创建
# def createtb():
#     db = pymysql.connect(host='127.0.0.1',
#                          port=3379,
#                          user='root',
#                          password='password',
#                          database='robosen_project'
#                          )
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # 使用预处理语句创建表
#     sql = """CREATE TABLE tbtest (
#              uid  CHAR(20) NOT NULL,
#              test_title  CHAR(20),
#              test_count INT,
#              test_content TEXT,
#              INCOME FLOAT )"""
#     cursor.execute(sql)
#
#     # 关闭数据库连接
#     db.close()

# 插入
# def inserttb():
#     db = pymysql.connect(host='127.0.0.1',
#                          port=3379,
#                          user='root',
#                          password='password',
#                          database='database'
#                          )
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # SQL 插入语句
#     sql = """INSERT INTO tbtest(uid,
#              test_title, test_count, test_content, INCOME)
#              VALUES ('123456','mom', 14, '233467689707897856', 200.75)"""
#
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 如果发生错误则回滚
#         db.rollback()
#
#     # 关闭数据库连接
#     db.close()

# # 查询
# def selecttb():
#     db = pymysql.connect(host='127.0.0.1',
#                          port=3379,
#                          user='root',
#                          password='password',
#                          database='database'
#                          )
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # SQL 查询语句
#     sql = "SELECT * FROM tbtest \
#            WHERE test_count > %s" % (12)
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 获取所有记录列表
#         results = cursor.fetchall()
#         for row in results:
#             uid = row[0]
#             test_title = row[1]
#             test_count = row[2]
#             test_content = row[3]
#             INCOME = row[4]
#             # 打印结果
#             print("%s,%s,%s,%s,%s" % (uid, test_title, test_count, test_content, INCOME))
#     except:
#         print("Error: unable to fetch data")
#
#         # 关闭数据库连接
#     db.close()

# 更新
# def updatetb():
#     db = pymysql.connect(host='127.0.0.1',
#                          port=3379,
#                          user='root',
#                          password='password',
#                          database='database'
#                          )
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # SQL 更新语句
#     sql = "UPDATE tbtest SET INCOME = 385.14 WHERE test_count >= 20"
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 发生错误时回滚
#         db.rollback()
#
#     # 关闭数据库连接
#     db.close()

# 增加字段
# def addlabtb():
#     db = pymysql.connect(host='127.0.0.1',
#                          port=3379,
#                          user='root',
#                          password='password',
#                          database='database'
#                          )
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # 布尔型在mysql数据库中存储类型为tinyint(1) 1代表true 0代表false
#     sql = 'ALTER TABLE tbtest ADD test_status TINYINT(1) DEFAULT FALSE'
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 发生错误时回滚
#         db.rollback()
#
#     # 关闭数据库连接
#     db.close()

# # 删除数据
# def deltb():
#     db = pymysql.connect(host='127.0.0.1',
#                              port=3379,
#                              user='root',
#                              password='password',
#                              database='database'
#                              )
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # SQL 删除语句
#     sql = "DELETE FROM tbtest WHERE INCOME >= %s" % (20)
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 提交修改
#         db.commit()
#     except:
#         # 发生错误时回滚
#         db.rollback()
#
#     # 关闭连接
#     db.close()

# if __name__ == '__main__':
    # crt = createtb()
    # int = inserttb()
    # sel = selecttb()
    # upd = updatetb()
    # add = addlabtb()
    # deltb = deltb()










