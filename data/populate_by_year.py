import MySQLdb


def open_connection():
    db = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='pass',
        db='freq_dict',
        charset='utf8',
        use_unicode=True
    )
    cursor = db.cursor()
    return db, cursor


def create_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS lemmata_by_year ("
                   "id integer primary key auto_increment not null,"
                   "lemma char(50),"
                   "fiction_50_60 decimal(10,1),"
                   "fiction_70_80 decimal(10,1),"
                   "fiction_90_00 decimal(10,1),"
                   "news_50_60 decimal(10,1),"
                   "news_70_80 decimal(10,1),"
                   "news_90_00 decimal(10,1)"
                   ");")


def populate(db, cursor):
    f = open('lemmata_by_year.tsv', 'r')
    for line in f:
        line = line.rstrip().split('\t')
        cmd = 'INSERT INTO lemmata_by_year (lemma, fiction_50_60, fiction_70_80, fiction_90_00,' \
              'news_50_60, news_70_80, news_90_00)' \
              'VALUES ("{}",{},{},{},{},{},{})'.format(*line)
        cursor.execute(cmd)
    db.commit()


def check(cursor):
    cmd = 'SELECT * FROM lemma_freq WHERE lemma="человек"'
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
    # check(cursor)
    close_connection(db)

if __name__ == '__main__':
    main()
