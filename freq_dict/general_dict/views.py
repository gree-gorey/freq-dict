from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from general_dict.models import General, ByYear, ByGenre
from gram_dict_query.query import get_lemma_table, get_wordform_table


def index(request):
    return render(request, 'index.html')


def parse_req(request, m):
    arr_l = []
    arr_p = []
    for i in request.GET:
        if 'lemma' in i:
            arr_l.append(i)
        elif 'pos' in i:
            arr_p.append(i)
    final = []
    if 'pos1' in request.GET:
        for l in arr_l:
            final.extend(list(m.objects.filter(lemma=request.GET[l])))
        return final
    for i in arr_l:
        for n in arr_p:
            final.extend(list(m.objects.filter(lemma=request.GET[i]).filter(pos=request.GET[n])))
    return final


def gen_dict(request):
    arr = parse_req(request, General)
    y = parse_req(request, ByYear)
    g = parse_req(request, ByGenre)
    context = {'mockup': General.objects.all()[:1000], 'years': ByYear.objects.all()[:1000],
               'genre': ByGenre.objects.all()[:1000]}
    if arr != []:
        context['mockup'] = arr
    if y != []:
        context['years'] = y
    if g != []:
        context['genre'] = g
    return render(request, 'gen_dict.html', context=context)


def gram_dict(request):
    context = {}
    search_type = 'lemma'
    if request.GET:
        if request.GET['lemma']:
            lemma = request.GET['lemma']
            context['lemma'] = lemma
            context['words'] = get_lemma_table(lemma=lemma)
        elif request.GET['word_form'] or request.GET['ratio_from'] or request.GET['ratio_to']:
            search_type = 'word_form'
            word_form = request.GET['word_form']
            context['word_form'] = word_form
            ratio_from = request.GET['ratio_from'] if request.GET['ratio_from'] else 0
            context['ratio_from'] = ratio_from
            ratio_to = request.GET['ratio_to'] if request.GET['ratio_to'] else 100
            context['ratio_to'] = ratio_to
            if word_form or request.GET['ratio_from'] or request.GET['ratio_to']:
                if not word_form:
                    word_form = '%'
                context['list_wordforms'] = get_wordform_table(wordform=word_form,
                                                               ratio_from=ratio_from,
                                                               ratio_to=ratio_to)
    context['search_type'] = search_type
    return render(request, 'gram_dict.html', context=context)


def about(request):
    return render(request, 'about.html')
