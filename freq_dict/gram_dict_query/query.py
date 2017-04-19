import os
# from .ssh import get_paradigm
# from .secrets import secrets
from secrets import secrets
from ssh import get_paradigm


def get_table(lemma='человек'):
    result = get_paradigm(
        lemma=lemma,
        user=secrets['DB_USER'],
        passwd=secrets['DB_PASS'],
        db='RNCgram'
    )
    word = {}
    for row in result:
        print(row)
        pos = row[5]
        if pos == 'S':
            word_form = row[1]
            freq = row[8]
            number, case = row[3].split('=')[1].split(',')
            key = case + number
            if key not in word:
                word[key] = [(word_form, freq)]
            else:
                word[key].append((word_form, freq))
    return word


if __name__ == '__main__':
    get_table()
