# Tela incial

def iniciar():
    print('                          Jogo Plantão Médico             ')
    print("              ===========================================")
    print(' Estamos iniciando mais um dia de plantão no Hospital Geral, onde 3 especialistas terão que começar seu plantão:')
    comeco = (input('Quando quiser começar, digite a palavra jogar:'))
    while comeco == 'jogar':
        selecao_especialista()
    else:
        print('Até logo então :)')


def selecao_especialista():
    user_in = int(input("Selecione seu especialista:\n 1 -pneumologista\n 2 - cardiologista\n 3 -neurologista \nDigite 1, 2 ou 3:"))
    if user_in == 1:
        print('Você escolheu a pneumologista.')
        paciente1()
    elif user_in == 2:
        print('Você escolheu o cardiologista.')
        paciente2()
    elif user_in == 3:
        return 'Você escolheu o neurologista.'
    else:
        print("Digite uma opção válida !")
        selecao_especialista()


# Caso o jogador morra
def paciente_morreu():
    print("Infelizmente paciente veio a óbito.")
    resposta = (input("Game Over!\n\nDigite J para jogar denovo! :"))
    while resposta == 'J':
        iniciar()
    else:
        print("Então tá, até a próxima.")


# História paciente1

def paciente1():
    resposta = input("Paciente com 13 anos deu entrada no hospital com quadro de pneumonia bacteriana,"
                     "\nque inicialmente foi tratada com antibióticos,"
                     "\nmas quadro evoluiu para um derrame pleural."
                     "\no que você faz ?\n A - Solicitar ultrassonografia\n B - Encaminhar para cirurgia \nDigite A ou B:")
    if resposta == 'A':
        print("Foi feita a drenagem do líquido na cavidade pleural.")
        paciente_sarou()
    elif resposta == 'B':
        print("Cirurgia deu errado.")
        paciente_morreu()
    else:
        print("Por favor, digite uma opção válida!")
        paciente1()


def paciente_sarou():
    resposta = input("paciente evolui de forma satisfatória a cirurgia"
                     "\no que você faz ?\n A - Fica em observação pós-cirurgia\n B - Dispensado \nDigite A ou B:")
    if resposta == 'A':
        print("e teve alta e concluimos com êxito a cirurgia.")
        paciente_sobreviveu()
    elif resposta == 'B':
        print("foi para casa e não tomou os devidos cuidados, contraiu uma infecção e veio a óbito.")

        paciente_morreu()
    else:
        print("Digite uma opção válida!")
        paciente_sarou()


def paciente_sobreviveu():
    resposta = input("Entretanto após alguns meses ele voltou a sentir dores fortes. \nA - Não procurou médico. \nB - Procurou médico \nC - procurou segunda opinião"
                     "\nDigite A , B ou C:")
    if resposta == 'A':
        print("Veio a óbito")
        paciente_morreu()
    elif resposta == 'B':
        print("Paciente refez a cirurgia e veio a óbito")
        paciente_morreu()
    elif resposta == 'C':
        print("Parabéns por você procurar uma segunda opinião, você sobreviveu!")
        paciente_venceu()
    else:
        print("Por favor, digite uma opção válida!")
        paciente_sobreviveu()


def paciente_venceu():
    resposta = input("Parabéns por sua jornada, vc sobreviveu ao Plantão Médico, deseja jogar novamente? (sim/não)")                
    if resposta == 'sim':
        iniciar()
    else:
        resposta == 'não'
        print("Obrigada por jogar!")

        
# História personagem2

def paciente2():
    resposta = input("Paciente com 66 anos, deu entrada no hospital com confusão mental,"
                     "\nalteração da fala, tontura,"
                     "\ne dor de cabeça sem causa aparente."
                     "\no que você faz ?\n A - solicitar tomografia computadorizada\n B - encaminhar para cirurgia \nDigite A ou B:")
    if resposta == 'A':
        print(" paciente passou por cirurgia e tem chances de sobreviver.")
        paciente_sarou02()
    elif resposta == 'B':
        print("Cirurgia deu errado.")
        paciente_morreu()
    else:
        print("Por favor, digite uma opção válida !")
        paciente2()


def paciente_sarou02():
    resposta = input("Com tratamento correto, paciente segue vida normalmente"
                     "\no que você faz ?\n A - FAz exames regulares a cada seis meses\n B -Dispensado \nDigite A ou B:")
    if resposta == 'A':
        print("Parabens, você continua cuidando da sua saúde e segue saudável.")
        paciente_sobreviveu02()
    elif resposta == 'B':
        print("você descuidou da sua saúde, não fez seus exames regulares e veio a óbito")

        paciente_morreu()
    else:
        print("Digite uma opção válida!")
        paciente_sarou02()


def paciente_sobreviveu02():
    resposta = input("Entretanto após 2 anos ao fazer novos exames paciente descobriu uma nova doença. \nA - Não procurou médico. \nB - Procurou medicina alternativa \nC - procurou segunda opinião"
                     "\nDigite A , B ou C:")
    if resposta == 'A':
        print("Veio a óbito")
        paciente_morreu()
    elif resposta == 'B':
        print(" Mesmo com novos tratamentos não resistiu")
        paciente_morreu()
    elif resposta == 'C':
        print("Parabéns por você procurar uma segunda opinião, você sobreviveu!")
        paciente_venceu02()
    else:
        print("Por favor, digite uma opção válida !")
        paciente_sobreviveu()


def paciente_venceu02():
    resposta = input("Voê é um jogador resiliente e também venceu o jogo, deseja jogar novamente? (sim/não)")                
    if resposta == 'sim':
        iniciar()

    elif resposta == 'não':
        print("Obrigada por jogar!")

iniciar()