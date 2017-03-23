import sshtunnel
import MySQLdb
import time
import os


connect_begin = time.time()
with sshtunnel.SSHTunnelForwarder(
        (os.environ['HOST'], 22),
        ssh_username=os.environ['SSH_USER'],
        ssh_password=os.environ['SSH_PASS'],
        remote_bind_address=('0.0.0.0', 3306),
        local_bind_address=('127.0.0.1', 3333)
) as tunnel:
    print('SSH Connection established')

    db = MySQLdb.connect(
        host='127.0.0.1',
        port=3333,
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASS'],
        db=os.environ['DB_NAME'],
        charset='utf8',
        use_unicode=True
    )
    print('DB connection established')

    cursor = db.cursor()

    query_begin = time.time()
    cursor.execute(
    "SELECT * FROM second_source_years t1 "
    # "LEFT JOIN first_source_years t2 "
    # "ON t1.slovoform2 = t2.slovoform1 "
    "WHERE lemma='лимитировать'")
    query_end = time.time()

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()

    # for row in data:
    #     print(row)
    print(data)

    db.close()

connect_end = time.time()

print('Query time: {}'.format(query_end - query_begin   ))
print('Connection time: {}'.format(connect_end - connect_begin))
