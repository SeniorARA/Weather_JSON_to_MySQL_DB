# import mysql.connector
#
#
# connection = mysql.connector.connect(
#     host='localhost',
#     user = 'root',
#     password = '030119501330',
#     database = 'sys'
# )
#
# cursor = connection.cursor()
#
#
# create_request_str = """
#     CREATE TABLE python_test_db(
#         id INT PRIMARY KEY NOT NULL,
#
#         weather_id INT,
#
#         name VARCHAR(250),
#
#         description VARCHAR(250),
#
#         temp FLOAT,
#
#         wind_speed FLOAT
#     )
# """
#
# insert_request_str = """
#     INSERT INTO {}(id, weather_id, name, description, temp, wind_speed)
#
#     VALUES(%s,%s,%s,%s,%s,%s)
# """
#
# select_request_str = """
#     SELECT * FROM {}
# """
#
#
# # def create_table(table_name = str, **columns):
# #     return
#
#
# def insert(table_name = str,id = int, weather_id = int, name = str, description = str, temp = float, wind_speed = float):
#     try:
#         cursor.execute(insert_request_str.format(table_name),(id, weather_id, name, description, temp, wind_speed))
#         connection.commit()
#         print(" Success! ")
#
#     except mysql.connector.Error as err:
#         print (err)
#
#
#
#     return;
#
#
# def select(table_name = str):
#     try:
#         cursor.execute(select_request_str.format(table_name))
#         results = cursor.fetchall()
#
#     except mysql.connector.Error as err:
#         return err
#
#
#
#     return results
#
#
#
#
#
