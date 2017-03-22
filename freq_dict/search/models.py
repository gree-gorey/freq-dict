from django.db import models


class FirstSourceYears(models.Model):
    word_id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    slovoform1 = models.CharField(max_length=200)
    number_1700_1710 = models.IntegerField(db_column='1700-1710')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1711_1720 = models.IntegerField(db_column='1711-1720')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1721_1730 = models.IntegerField(db_column='1721-1730')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1731_1740 = models.IntegerField(db_column='1731-1740')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1741_1750 = models.IntegerField(db_column='1741-1750')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1751_1760 = models.IntegerField(db_column='1751-1760')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1761_1770 = models.IntegerField(db_column='1761-1770')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1771_1780 = models.IntegerField(db_column='1771-1780')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1781_1790 = models.IntegerField(db_column='1781-1790')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1791_1800 = models.IntegerField(db_column='1791-1800')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1801_1810 = models.IntegerField(db_column='1801-1810')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1811_1820 = models.IntegerField(db_column='1811-1820')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1821_1830 = models.IntegerField(db_column='1821-1830')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1831_1840 = models.IntegerField(db_column='1831-1840')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1841_1850 = models.IntegerField(db_column='1841-1850')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1851_1860 = models.IntegerField(db_column='1851-1860')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1861_1870 = models.IntegerField(db_column='1861-1870')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1871_1880 = models.IntegerField(db_column='1871-1880')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1881_1890 = models.IntegerField(db_column='1881-1890')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1891_1900 = models.IntegerField(db_column='1891-1900')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1901_1910 = models.IntegerField(db_column='1901-1910')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1911_1920 = models.IntegerField(db_column='1911-1920')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1921_1930 = models.IntegerField(db_column='1921-1930')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1931_1940 = models.IntegerField(db_column='1931-1940')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1941_1950 = models.IntegerField(db_column='1941-1950')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1951_1960 = models.IntegerField(db_column='1951-1960')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1961_1970 = models.IntegerField(db_column='1961-1970')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1971_1980 = models.IntegerField(db_column='1971-1980')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1981_1990 = models.IntegerField(db_column='1981-1990')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1991_2000 = models.IntegerField(db_column='1991-2000')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2001_2010 = models.IntegerField(db_column='2001-2010')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'first_source_years'

    def __str__(self):
        return self.slovoform1


class SecondSourceYears(models.Model):
    word_id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    slovoform2 = models.CharField(max_length=200)
    lemma = models.CharField(max_length=200)
    partofsp = models.CharField(db_column='partOfSp', max_length=50)  # Field name made lowercase.
    grammar = models.CharField(max_length=200)
    omonim = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'second_source_years'

    def __str__(self):
        return self.slovoform2
