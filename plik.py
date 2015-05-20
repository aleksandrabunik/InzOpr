import string
import operator

ile_dokumentow = int(input())
dokumenty=[]

for i in range(ile_dokumentow):
    dokumenty.append(input().lower())

ile_zapytan=int(input())
zapytania=[]

for i in range(ile_zapytan):
    zapytania.append(input())

indeks = dict()
nr_dokumentu=0

for d in dokumenty:
    d_pom = d
    for p in string.punctuation:
        d_pom=' '.join(d_pom.split(p))
    d_lista = d_pom.split()
    for wyraz in d_lista:
        if wyraz not in indeks:
            indeks[wyraz] = dict()
        if nr_dokumentu not in indeks[wyraz]:
            indeks[wyraz][nr_dokumentu] = 0
        indeks[wyraz][nr_dokumentu]+=1
    nr_dokumentu+=1

for z in zapytania:
    try:
        l = list(indeks[z.strip()].items())
        l0=sorted(l)
        l1=sorted(l0, key = operator.itemgetter(1), reverse = True)
        print( [i[0] for i in l1])
    except:
        print([]) 
