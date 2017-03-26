import MySQLdb
import os


def open_connection():
    db = MySQLdb.connect(
        host='localhost',
        user=os.environ['MYSQL_LOCAL_USER'],
        passwd=os.environ['MYSQL_LOCAL_PASS'],
        db='freq_dict',
        charset='utf8',
        use_unicode=True
    )
    cursor = db.cursor()
    return db, cursor


def create_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS lemmata_fiction ("
                   "id integer primary key auto_increment not null,"
                   "lemma char(50),"
                   "pos char(20),"
                   "freq_ipm decimal(10,1)"
                   ");")


def populate(db, cursor):
    f = open('lemmata_fiction.tsv', 'r')
    for line in f:
        line = line.rstrip().split('\t')
        cmd = 'INSERT INTO lemmata_fiction (lemma, pos, freq_ipm) ' \
              'VALUES ("{}","{}",{})'.format(*line)
        cursor.execute(cmd)
    db.commit()


def check(cursor):
    cmd = 'SELECT * FROM lemmata_fiction WHERE lemma="человек"'
    cursor.execute(cmd)
    # data = cursor.fetchall()
    data = cursor.fetchone()
    print(data)
    # for row in data:
    #     print(row)


def close_connection(db):
    db.close()


def main():
    db, cursor = open_connection()
    create_table(cursor)
    populate(db, cursor)
    check(cursor)
    close_connection(db)

if __name__ == '__main__':
    main()
