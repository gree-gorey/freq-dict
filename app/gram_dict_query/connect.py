import MySQLdb


def get_paradigm(lemma, user, passwd, db):
    db = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user=user,
        passwd=passwd,
        db=db,
        charset='utf8',
        use_unicode=True
    )
    print('DB connection established')
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM std2013 "
        "WHERE Lex like '{}'".format(lemma)

    )
    data = cursor.fetchall()
    db.close()
    return data


def get_wordforms(wordform, ratio_from, ratio_to, user, passwd, db):
    db = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user=user,
        passwd=passwd,
        db=db,
        charset='utf8',
        use_unicode=True
    )
    print('DB connection established')
    cursor = db.cursor()
    cursor.execute(
        "SELECT Word, Lex, FreqAbs, Gr, ratio FROM std2013 "
        "WHERE Word like '{}' "
        "AND "
        "ratio BETWEEN {} AND {}"
        "".format(wordform, ratio_from, ratio_to)
    )
    data = cursor.fetchall()
    db.close()
    return data


def main():
    pass


if __name__ == '__main__':
    main()
