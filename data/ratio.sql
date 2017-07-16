-- временная табличка с результатами запроса из главной таблицы
create temporary table if not exists lemmata as (
	select Lex, sum(FreqAbs) as sum_freq
	from std2013
	group by Lex
	)
;

UPDATE std2013 JOIN
lemmata
on std2013.Lex = lemmata.Lex
SET std2013.ratio = std2013.FreqAbs / lemmata.sum_freq * 100;



SELECT Word, Lex, FreqAbs, Gr, ratio FROM std2013 WHERE ratio BETWEEN 70 AND 90 limit 10;
