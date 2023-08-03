import time
# Bem Vindo
print("Bem-vindo ao Info AIR")
print("Sabemos que um fator determinante para sua saude e a umidade do ar!")
resposta = input("Voce gostaria de realizar um teste para saber a umidade do ar da sua regiao? (s/n) ")


# se responder errado:
while not (resposta == "s" or resposta == "n"):
    print("Responda com s ou n porfavor")
    resposta = input("Voce gostaria de realizar um teste para saber a umidade do ar da sua regiao? (s/n) ")

if resposta == "s":
    umidade = 0

    # input Mora perto do litoral ou de rios?
    agua = input("Voce mora próximo à areas que tenham água? ex: Litoral, perto de rios, etc (s/n) ")
    if agua == "s":
        umidade += 1
    else:
        umidade -= 1

    # input Temperatura
    sensacao_terminca = input("A sensação térmica esta mais alta do que a temperatura? (s/n) ")
    if sensacao_terminca == "s":
        umidade += 2
    else:
        umidade -= 1

    # input Ocorrencia de chuvas
    chuva = input("Choveu nos ultimos dias? (s/n) ")
    if chuva == "s":
        umidade += 1
    else:
        umidade -= 1

    # Resultado do codigo
    if umidade >= 3:
        print("A umidade do ar esta ALTA")
        print("A alta umidade favorece o aparecimento de mofo, fungos, ácaros e bolores, afetando pessoas que possuem problemas respiratórios, como rinite, sinusite e asma")
        print("Se voce possui alguma dessas doencas e bom se prevenir")
    else:
        print("A umidade do Ar esta BAIXA")
        print('A baixa umidade do ar pode gerar garganta seca, excesso de catarro, pele coçando, dores de cabeça e sensação de areia nos olhos são alguns dos efeitos que a baixa umidade provoca, além do risco do desenvolvimento infecções pulmonares, crises alérgicas, amigdalites, faringites e sinusites.')
        print("Procure manter o corpo sempre bem hidratado, Lave as mãos com frequência e evite colocá-las na boca e no nariz")
    time.sleep(1)
    print("OBS: Nossos calculos sao realizados conforme os dados iseridos!")
    print("Considere visitar nosso site para informacoes mais precisas sobre sua regiao!")
    print("Agradecemos sua visita")
else:
    print("Foi um prazer atende-lo")

'''
Nome dos componentes – 1ESPX
Caique Walter Silva – RM550693
Gabriel Pacheco – RM550191
Guilherme Nobre Bernardo – RM98604
Gustavo Verissímo de Paulo Ales –RM551244
Maitê Savicius – RM98435
Murilo Henrique – RM99855
'''