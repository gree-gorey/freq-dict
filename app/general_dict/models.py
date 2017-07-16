from django.db import models

class General(models.Model):
	"""General"""
	lemma = models.CharField(max_length=100)
	pos = models.CharField(max_length=100)
	freq_ipm = models.FloatField()
	segm_range = models.IntegerField()
	d_coeff = models.IntegerField()
	doc = models.IntegerField()

	def __str__(self):
		return self.lemma+'_'+self.pos

def adddata():
	datapath = '/home/religofsil/freq-dict/data/lemmata_all.tsv'
	with open(datapath) as f:
		for line in f:
			l = line.split('\t')
			m = General(lemma=l[0], pos=l[1], freq_ipm=l[2], segm_range=l[3], d_coeff=l[4], doc=l[5])
			m.save()
	print('done')

class ByYear(models.Model):
	"""ByYear"""
	lemma = models.CharField(max_length=100)
	pos = models.CharField(max_length=100)
	fiction_50_60 = models.FloatField()
	fiction_70_80 = models.FloatField()
	fiction_90_00 = models.FloatField()
	news_50_60 = models.FloatField()
	news_70_80 = models.FloatField()
	news_90_00 = models.FloatField()

	def __str__(self):
		return self.lemma+'_'+self.pos


class ByGenre(models.Model):
	"""ByGenre"""
	lemma = models.CharField(max_length=100)
	pos = models.CharField(max_length=100)
	freq_spoken = models.FloatField()
	freq_news = models.FloatField()
	freq_fiction = models.FloatField()
	freq_nonfiction = models.FloatField()

	def __str__(self):
		return self.lemma+'_'+self.pos
