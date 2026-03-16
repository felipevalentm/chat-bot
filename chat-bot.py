
intencoes = {
    "saudacao": ["oi", "olá", "bom", "dia", "boa", "tarde", "tudo", "bem"],
    "compra": ["comprar", "pedido", "adquirir", "preço"],
    "despedida": ["tchau", "até", "logo", "falou"]
    }

resposta = {
    "saudacao": "oi. bem-vindo",
    "compra": "o que deseja comprar?",
    "despedida" : "tchau!",
    }

while True:
        frase_inicial = input("Usuário: ").replace(".", "").replace("?", "").replace("!", "").replace(",", "").lower().split()
        intencao = None

        for x in frase_inicial:

            for chave in intencoes:
                 if x in intencoes[chave]:
                      intencao = chave
                      break

        if intencao:
            print("Bot: ", resposta[intencao])
        else:
            print("Não identificamos sua resposta!")

 
