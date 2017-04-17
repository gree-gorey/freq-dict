# import MySQLdb
#
# # Open database connection
# db = MySQLdb.connect(
#     host='localhost',
#     user='root',
#     passwd='pass',
#     db='freq_dict',
#     charset='utf8',
#     use_unicode=True
# )
#
# # prepare a cursor object using cursor() method
# cursor = db.cursor()
#
# # execute SQL query using execute() method.
# cursor.execute("SELECT * FROM second_source_years t1 LEFT JOIN first_source_years t2 ON t1.slovoform2 = t2.slovoform1 WHERE lemma='лимитировать'")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchall()
#
# for row in data:
#     print(row)
#
# # disconnect from server
# db.close()

import mysql.connector


