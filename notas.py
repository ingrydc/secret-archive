# sistema de notas baseado na quantidade de faltas
# se o aluno tiver mais de 10 faltas, afetará diretaente o conceito da nota

nota = float(input('Digite sua nota: '))
faltas = int(input('Digite o número de faltas: '))

if faltas <= 10:
    if nota < 60:
        print('Seu conceito é C.')
    elif nota >= 60 and nota < 85:
        print('Seu conceito é B.')
    else:
        print('Seu conceito é A.')

else:
    if nota < 60:
        print('Seu conceito é D.')
    elif nota >= 60 and nota < 85:
        print('Seu conceito é C.')
    else:
        print('Seu conceito é B.')
