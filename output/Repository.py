import mysql.connector
# import random
#
#
# class Conclusion():
#     def __init__(self):
#         self.DATABASE = mysql.connector.connect(host='localhost', user='root', password='1234', database='films')
#         self.MY_CURSOR = self.DATABASE.cursor(buffered=True)
#         self.table_name = ''
#         self.count = ''
#
#     def change_const(self):
#         self.table_name = ''
#
#     def init_random_value(self):
#         self.change_const()
#         self.filmsID=[]
#         self.MY_CURSOR.execute(f'SELECT * FROM {self.table_name}')
#         self.count = self.MY_CURSOR.rowcount
#         for self.n in range(5):
#             self.n = random.randint(0, self.count)
#             self.filmsID.append(self.n)
#         return self.filmsID
#
#     def output(self, values):
#         self.row = self.MY_CURSOR.fetchall()
#         b = []
#         for self.i in range(len(values)):
#             d = (
#                   f'🗓 <b>Title:</b> {self.row[values[self.i]][1]} 🗓\n'
#                   f'🪐 <b>Description:</b> {self.row[values[self.i]][2]} 🪐\n'
#                   f'👾 <b>Producer:</b> {self.row[values[self.i]][3]} 👾\n'
#                   f'📽 <b>Link:</b> {self.row[values[self.i]][4]} 📽\n')
#             return d

DATABASE = mysql.connector.connect(host='localhost', user='root', password='1234', database='films', auth_plugin='mysql_native_password')