import sqlite3
from sqlite3.dbapi2 import Error

# 创建连接数据库的函数
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# 新建 rasa.db 数据库和 UserInfo 表格
def create_database():
    database = "rasa.db"
    conn = create_connection(database)
    cursor = conn.cursor()

    # 创建 UserInfo 表格
    cursor.execute('''CREATE TABLE IF NOT EXISTS UserInfo 
                      (ID TEXT, email TEXT, order_number TEXT, category TEXT)''')

    # 读取 order.txt 文件并分行处理数据
    with open('order.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            # 提取每行数据并进行插入操作
            data = line.strip().split(',')
            cursor.execute("INSERT INTO UserInfo VALUES (?, ?, ?, ?)", data)

    # 提交更改并关闭数据库连接
    conn.commit()
    conn.close()

# 运行 create_database() 函数以创建数据库和表格，并插入数据
create_database()


# 用户注册账号并存储到数据库
def register_user(user_id, email):
    database = "rasa.db"
    conn = create_connection(database)
    cursor = conn.cursor()

    sql = 'INSERT INTO UserInfo (ID, email) VALUES (?, ?)'
    cursor.execute(sql, (user_id, email))
    conn.commit()
    conn.close()

# 根据 order_number 查询订单信息
def get_order_info_by_number(order_number):
    database = "rasa.db"
    conn = create_connection(database)
    cursor = conn.cursor()

    sql = 'SELECT * FROM UserInfo WHERE order_number = ?'
    cursor.execute(sql, (order_number,))
    order_info = cursor.fetchone()
    conn.close()

    return order_info

# # 更新待联系字段为“yes”
# def update_contact_status(email):
#     database = "rasa.db"
#     conn = create_connection(database)
#     cursor = conn.cursor()

#     sql = "UPDATE UserInfo SET to_be_contacted = 'yes' WHERE email = ?"
#     cursor.execute(sql, (email,))
#     conn.commit()
#     conn.close()
    
if __name__ == '__main__':
    user_id = input("请输入用户ID: ")
    email = input("请输入邮箱: ")
    register_user(user_id, email)
    print("注册成功！")

    order_number = input("请输入订单号: ")
    order_info = get_order_info_by_number(order_number)
    if order_info:
        print("订单信息：", order_info)
    else:
        print("找不到该订单！")

 