f1 = open('lemmata_fiction.tsv')
f2 = open('lemmata_news.tsv')
f3 = open('lemmata_nonfiction.tsv')
f4 = open('lemmata_spoken.tsv')

arr = []
helper_fi = []
helper_ne = []
helper_nf = []
helper_sp = []

class Word(object):
	"""docstring for ClassName"""
	def __init__(self, lemma, pos, fiction=0, news=0, nonfiction=0, spoken=0):
		self.lemma = lemma
		self.pos = pos
		self.fiction = fiction
		self.news = news
		self.nonfiction = nonfiction
		self.spoken = spoken


for line in f1:
	l = line.split('\t')
	helper_fi.append(l[0]+'_'+l[1])
	arr.append(Word(l[0], l[1], l[2].strip()))
f1.close()

for line in f2:
	l = line.split('\t')
	if l[0]+'_'+l[1] not in helper_fi:
		arr.append(Word(l[0], l[1], news=l[2].strip()))
	else:
		for i in arr:
			if i.lemma==l[0] and i.pos==l[1]:
				i.news=l[2].strip()
				helper_fi.append(i.lemma+'_'+i.pos)
				break
f2.close()

for line in f3:
	l = line.split('\t')
	if l[0]+'_'+l[1] not in helper_fi:
		arr.append(Word(l[0], l[1], nonfiction=l[2].strip()))
	else:
		for i in arr:
			if i.lemma==l[0] and i.pos==l[1]:
				i.nonfiction=l[2].strip()
				helper_fi.append(i.lemma+'_'+i.pos)
				break
f3.close()

for line in f4:
	l = line.split('\t')
	if l[0]+'_'+l[1] not in helper_fi:
		arr.append(Word(l[0], l[1], spoken=l[2].strip()))
	else:
		for i in arr:
			if i.lemma==l[0] and i.pos==l[1]:
				i.spoken=l[2].strip()
				helper_fi.append(i.lemma+'_'+i.pos)
				break
f4.close()

with open('allbygenre.tsv', 'w') as f:
	for i in arr:
		f.write(i.lemma+'\t'+i.pos+'\t'+str(i.fiction)+'\t'+str(i.news)+'\t'+str(i.nonfiction)+'\t'+str(i.spoken)+'\n')