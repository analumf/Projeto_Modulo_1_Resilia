def quebra_linha():
    print('=' * 40)

def escolha_personagem():
    escolha = int(input('escolha uma opção para começar a jogar: \n[1] [2] [3]\n'))
    if escolha == 1:
    
        print('Cirurgia Pulmonar:')
        print('Paciente com 13 anos deu entrada no hospital com quadro de pneumonia bacteriana,')
        print('que inicialmente foi tratada com antibióticos,')
        print('mas quadro evoluiu para um derrame pleural.')

    elif escolha == 2:
        print('cirurgia neuro')
        print('Paciente com 66 anos, deu entrada no hospital com confusão mental,')
        print('alteração da fala e no andar e dor de cabeça sem causa aparente') 



    elif escolha == 3:
        print('cirurgia cardio')    
    else:
        print('escolha uma opção válida')
        quebra_linha()
        jogador_morre()
        escolha_personagem()
      
        

print('#######################################################################')

print('Bem Vindo ao jogo Plantão Médico')

print('###############################################################################################################')

print('Estamos iniciando mais um dia de plantão no Hospital Geral, onde 3 especialistas terão que começar seu plantão:')

print('1- Pneumologista:')

print('Uma das médicas mais talentosas do nosso hospital, Dra. Lívia wesley é competente e eficaz.')
print('Intensa e confiante, ela não admite erros e por isso tem uma cobrança interna muito grande.')
print('Solteira, se dedica totalmente ao seu trabalho.')
print('Tem uma relação proxima com a diretora, Dra. Ana Mendes.')

quebra_linha()

print('2- Cardiologista:')

print('Dra. Cristina Chase é uma médica especializada em transplantes de coração,')
print('muito eficaz e apaixonada por cardiologia, dedita atenção especial para cada paciente,')
print('tenta conciliar a vida profissional com a pessoal sem sucesso,')
print('e superar preconceitos enfrentados dentro do trabalho que é dominado por homens.')

quebra_linha()

print(' 3- Neurologista:')

print('Dr. Roberto Rhodes é um neurocirurgião muito procurado por descobrir doenças que nenhum outro profissional é capaz de desvendar.')
print('Por isso é arrogante e quase sempre não escuta os outros.')
print('Não tem uma relação familiar boa e enfrenta problemas alcoólicos.')

escolha_personagem()







