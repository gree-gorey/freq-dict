from django.conf import settings
from .connect import get_paradigm, get_wordforms
# from connect import get_paradigm, get_wordforms


def get_lemma_table(lemma='стол%'):
    result = get_paradigm(
        lemma=lemma,
        user=settings.MYSQL_USER,
        passwd=settings.MYSQL_PASSWORD,
        db=settings.MYSQL_DB
    )
    words = {}
    for row in result:
        # print(row)
        lemma = row[2]
        if lemma not in words:
            words[lemma] = {}
        pos = row[5]
        if pos == 'S':
            word_form = row[1]
            freq = row[8]
            ratio = row[19]
            first_labels = row[3].split('=')[0].split(',')
            second_labels = row[3].split('=')[1].split(',')
            labels = first_labels + second_labels
            number = 'pl' if 'pl' in labels else 'sg'
            case = second_labels[1] if len(second_labels) > 1 else second_labels[0]
            key = case + number
            if key not in words[lemma]:
                words[lemma][key] = [(word_form, freq, ratio)]
            else:
                words[lemma][key].append((word_form, freq, ratio))
    return words


def get_wordform_table(wordform='стола%', ratio_from=0, ratio_to=100):
    result = get_wordforms(
        wordform=wordform,
        ratio_from=ratio_from,
        ratio_to=ratio_to,
        user=settings.MYSQL_USER,
        passwd=settings.MYSQL_PASSWORD,
        db=settings.MYSQL_DB
    )
    return result


if __name__ == '__main__':
    table = get_wordform_table()
    print(table)
