import sshtunnel
import MySQLdb
import os
# from .secrets import secrets
from secrets import secrets


def ssh_decorator(host, ssh_user, ssh_passwd):
    def inner_ssh_decorator(func):
        def func_wrapper(lemma, user, passwd, db):
            with sshtunnel.SSHTunnelForwarder(
                    (host, 22),
                    ssh_username=ssh_user,
                    ssh_password=ssh_passwd,
                    remote_bind_address=('0.0.0.0', 3306),
                    local_bind_address=('127.0.0.1', 3333)
                    ) as tunnel:
                print('SSH Connection established')
                output = func(lemma, user, passwd, db)
            return output
        return func_wrapper
    return inner_ssh_decorator

# @ssh_decorator(host=os.environ['HOST'], ssh_user=os.environ['SSH_USER'], ssh_passwd=os.environ['SSH_PASS'])
@ssh_decorator(host=secrets['HOST'], ssh_user=secrets['SSH_USER'], ssh_passwd=secrets['SSH_PASS'])
def get_paradigm(lemma, user, passwd, db):
    db = MySQLdb.connect(
        host='127.0.0.1',
        port=3333,
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
        "WHERE Lex='{}'".format(lemma)

    )
    data = cursor.fetchall()
    db.close()
    return data


def main():
    pass


if __name__ == '__main__':
    main()
