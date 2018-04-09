# -*- coding: utf-8 -*-
print "CSI forenzični program"

znacaji = {
    'hair': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC'
    },
    'face': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA'
    },
    'eyes': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC'
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC'
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG'
    }
}

osumljeni = {
    'Eva': {
        'hair': 'blonde',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'female',
        'race': 'white'
    },
    'Larisa': {
        'hair': 'brown',
        'face': 'oval',
        'eyes': 'brown',
        'gender': 'female',
        'race': 'white'
    },
    'Matej': {
        'hair': 'black',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'male',
        'race': 'white'
    },
    'Miha': {
        'hair': 'brown',
        'face': 'square',
        'eyes': 'green',
        'gender': 'male',
        'race': 'white'
    }
}

dna_file = open('dna.txt', 'r')
dna = dna_file.read()
dna_file.close()

osumljen = {}

for znacaj, lastnosti in znacaji.iteritems():
    for znacaji, zaporedje in lastnosti.iteritems():
        if dna.find(zaporedje) != -1:
            osumljen[znacaj] = znacaji
            break

ime = ''

for ime, lastnosti in osumljeni.iteritems():
    trenutno_ime = ''
    for znacaj, lastnost in lastnosti.iteritems():
        if osumljen[znacaj] == lastnost:
            trenutno_ime = ime
            break
        else:
            trenutno_ime = ''
            break

    if trenutno_ime:
        print "Oseba ki je pojedla sladoled je %s." % trenutno_ime
        break