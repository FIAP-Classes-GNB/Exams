# Variáveis Globais
valid = ["s", "n"]
menu = ["Sobre a InfoAir", "Teste de qualidade do ar", "Entre em contato conosco", "Sair"]
menu_n = ["1", "2", "3", "4"]
send_options = ["enviar", "cancelar", "refazer"]

# Funções

def valid_list(question, options):
    option = input(question)
    while True:
        if option not in options:
            option = input(f"Por favor, selecione uma opção válida. [{string_list(options)}] ")
            continue
        return option

def string_list(options):
    concat= ""
    for i in range(len(options)):
        concat += options[i]
        if i != len(options)-1:
            concat+= "/"
    return concat

def valida_email(pergunta):
    while True:
        email = input(pergunta)
        has_at = False
        has_dot = False

        for i in email:
            if i == "@":
                has_at = True
            if i == ".":
                has_dot = True

        if has_at and has_dot:
            return email
        else:
            print("Email Inválido.")

def pergunta_quiz(question, answers, results):
    answer= valid_list(question, answers)
    for i in range(len(answers)):
        if answer == answers[i]:
            return results[i]

# Telas

def tela_menu():
    print("\nInforme para nós o que está buscando: ")
    for i in range(len(menu)):
        print(f"[{i + 1}] - {menu[i]}")
    return valid_list("", menu_n)


def tela_sobre():
    print("\nSOBRE")

    print("   A InfoAir é uma empresa especializada em fornecer serviços confiáveis de monitoramento e avaliação da \nqualidade do ar para empresas e indivíduos preocupados com a saúde e o meio ambiente.")
    print("   Somos uma pequena empresa dedicada a ajudar nossos clientes a entender melhor a qualidade do ar em suas \náreas de atuação. Fundada por um grupo de especialistas em saúde ambiental e tecnologia, nós nos esforçamos \npara fornecer informações precisas e acessíveis sobre os níveis de poluentes atmosféricos em diferentes ambientes.")
    print("   Com nossa tecnologia avançada de monitoramento da qualidade do ar, nós coletamos dados em tempo real \nsobre os níveis de poluentes em diversas regiões. Nossa equipe de especialistas em saúde ambiental analisa esses \ndados e os traduz em relatórios claros e objetivos para nossos clientes.")
    print("   Acreditamos que todos têm o direito de saber a qualidade do ar que estão respirando e como isso pode \nafetar sua saúde e o meio ambiente. Por isso, nos dedicamos a fornecer informações precisas e confiáveis sobre a \nqualidade do ar em diferentes ambientes, desde escritórios a áreas industriais.")
    print("   Na  InfoAir estamos comprometidos com a proteção da saúde e do meio ambiente. Nosso trabalho contribui \npara um mundo mais saudável e sustentável. Entre em contato conosco para saber mais sobre nossos serviços de \nmonitoramento e avaliação da qualidade do ar.")

    input("\nPressione [Enter] para voltar ao menu.")
    return


def tela_quiz():
    print("\nQUIZ")
    print("   Nosso quiz tem como objetivo te ajudar a identificar se a umidade do ar da sua região está alta ou baixa, \nassim saberemos como te informar quais possíveis problemas que você pode enfrentar no seu dia-a-dia.")

    start = valid_list(f"\nIniciar Quiz? [{string_list(valid)}] ", valid)

    if start == "s":
        while True:
            # Perguntas
            humidity = 0
            humidity += pergunta_quiz(f"1) Você mora próximo à áreas que tenham água? ex: Litoral, perto de rios, etc [{string_list(valid)}] ", valid, [1,-1])
            humidity += pergunta_quiz(f"2) A sensação térmica esta mais alta do que a temperatura? [{string_list(valid)}] ", valid, [2,-1])
            humidity += pergunta_quiz(f"3) Choveu nos últimos dias? [{string_list(valid)}] ", valid, [1,-1])

            # Resultado
            if humidity >= 3:
                print("\nA umidade do ar esta ALTA.\nA alta umidade favorece o aparecimento de mofo, fungos, ácaros e bolores, afetando pessoas que possuem problemas respiratórios, como rinite, sinusite e asma.\nSe você possui alguma dessas doenças e bom se prevenir.")
            else:
                print("\nA umidade do Ar esta BAIXA.\nA baixa umidade do ar pode gerar garganta seca, excesso de catarro, pele coçando, dores de cabeça e sensação de areia nos olhos são alguns dos efeitos que a baixa umidade provoca, além do risco do desenvolvimento infecções pulmonares, crises alérgicas, amigdalites, faringites e sinusites.\nProcure manter o corpo sempre bem hidratado, Lave as mãos com frequência e evite colocá-las na boca e no nariz.")
            print("OBS: Nossos cálculos são realizados conforme os dados iseridos!")

            # Repetir?
            again= valid_list(f"\nGostaria de realizar um novo teste? [{string_list(valid)}] ",valid)
            if again == "s":
                continue
            else:
                break
    else:
        print("Entendo, se mudar de idéia estamos disponíveis a qualquer momento, foi um prazer atende-lo")

    input("\nPressione [Enter] para voltar ao menu.")
    return


def tela_contato():
    print("\nCONTATO")
    print("   Agradecemos seu interesse em nossos serviços. Se você tiver alguma dúvida, comentário ou desejar mais \ninformações, por favor, entre em contato conosco preenchendo o formulário abaixo. Nossa equipe terá prazer em \najudá-lo.")

    start= valid_list(f"\nIniciar preenchimento de Formulário? [{string_list(valid)}] ", valid)
    if start == "s":
        while True:
            print("\nFORMULÁRIO")

            name = input("Informe seu nome completo: ")
            email= valida_email("E-mail para contato: ")
            subject = input("Qual o motivo do contato? ")
            message = input("Digite sua mensagem: ")
            print(f"\nDe: {email} ({name})\nPara: contato@infoair.com\nAssunto: {subject}\nConteúdo: {message}")

            send= valid_list(f"\nEstá contente com a mensagem a ser enviada? [{string_list(send_options)}] ", send_options)
            if send == "enviar":
                # Envio simbólico da mensagem
                sent = f"\nDe: {email} ({name})\nPara: contato@infoair.com\nAssunto: {subject}\nConteúdo: {message}"
                print("Mensagem enviada com sucesso! Entraremos em contato em breve.")
                break
            elif send == "cancelar":
                print("Envio de mensagem cancelado.")
                break

    input("\nPressione [Enter] para voltar ao menu.")
    return


# Programa

print("Bem-vindo ao InfoAIR!")
while True:
    nav=tela_menu()
    if nav == "1":
        tela_sobre()
    elif nav == "2":
        tela_quiz()
    elif nav == "3":
        tela_contato()
    else:
        print("\nConsidere visitar nosso site novamente para mais informações, agradecemos sua visita!")
        break

'''
Nome dos componentes – 1ESPX
Caique Walter Silva – RM550693
Gabriel Pacheco – RM550191
Guilherme Nobre Bernardo – RM98604
Gustavo Verissímo de Paulo Ales –RM551244
Maitê Savicius – RM98435
Murilo Henrique – RM99855
'''