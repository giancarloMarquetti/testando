# def comparaValores(vl1,vl2):
#     assert(vl1 == vl2)

# comparaValores(3,4)

# Na classe acima apresentou erro então vou corrigir no código abaixo.
# assert sempre tem que ser verificado com modo boleano

def comparaValores(vl1,vl2):
    if(vl1 != vl2):
        vl1 = vl2
    assert(vl1 == vl2)

def obtemEscola(escola):
    if(escola != 'Proway'):
        escola = 'Proway'
    assert(escola == 'Proway')

def validaIdade(ano):
    idade = 2024 - ano
    assert(idade >= 18)

comparaValores(3,4)
obtemEscola('SOS')
validaIdade(2010)