"""
Desenvolver um sistema de perguntas e respostas utilizando tudo visto até o momento nas aulas
"""

print()
print('Escolha apenas a letra da resposta, a, b, ou c')

perguntas = { #cria o dicionario geral perguntas
    'Pergunta 1': { #cria outro dicionario pergunta 1
        'pergunta': 'Quanto é 2+2? ',
        'respostas': { #cria outro dicionario respostas
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items(): #cria um laço pra percorrer o dicionario perguntas
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items(): #cria um laço pra percorrer o dicionario respostas
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']: #verifica se a resposta digitada esta correta
        print('resposta certa')
        respostas_certas += 1
    else:
        print('resposta errada')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')
