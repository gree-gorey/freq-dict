-- временная табличка с результатами запроса из главной таблицы
create temporary table if not exists q_init as (
	select lemma, pos, freq_ipm, segm_range, d_coeff, doc
	from lemmata_all
	where lemma="человек"
	)
;


-- леммы из запроса по стилям
select q_sp_news_fi.lemma, q_sp_news_fi.pos, q_sp_news_fi.freq_spoken, q_sp_news_fi.freq_news, q_sp_news_fi.freq_fiction, non.freq_ipm as "freq_nonfiction" from (
	select q_sp_news.lemma, q_sp_news.pos, q_sp_news.freq_spoken, q_sp_news.freq_news, fi.freq_ipm as "freq_fiction" from (
		select q_sp.lemma, q_sp.pos, q_sp.freq_spoken, news.freq_ipm as "freq_news" from (
			select q.lemma, q.pos, sp.freq_ipm as "freq_spoken" from (
				select lemma, pos
				from q_init
			) q
			left join lemmata_spoken sp
			on q.lemma=sp.lemma and q.pos=sp.pos
			) q_sp
		left join lemmata_news news
		on q_sp.lemma=news.lemma and q_sp.pos=news.pos
		) q_sp_news
	left join lemmata_fiction fi
	on q_sp_news.lemma=fi.lemma and q_sp_news.pos=fi.pos
	) q_sp_news_fi
left join lemmata_nonfiction non
on q_sp_news_fi.lemma=non.lemma and q_sp_news_fi.pos=non.pos
;


-- леммы из запроса по годам
select q.lemma, q.pos, years.fiction_50_60, years.fiction_70_80, years.fiction_90_00,
years.news_50_60, years.news_70_80, years.news_90_00 from (
	select lemma, pos
	from q_init
) q
left join lemmata_by_year years
on q.lemma=years.lemma and q.pos=years.pos
;


-- все леммы по алфавиту
select *
from lemmata_all
order by lemma
limit 10
;


-- все леммы по частоте
select *
from lemmata_all
order by freq_ipm desc
limit 10
;



