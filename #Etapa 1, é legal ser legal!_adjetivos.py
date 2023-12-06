#Etapa 1, é legal ser legal!

from random import*
print("Gerador de cumprimentos")
print("-"*10)

cumprimentos=["Exelente trabalho.Realmente muito bem feito.",
                "Suas habilidades de programação são muito, muito boas.",
                "Você é um humano exelente."
              ]

#imprime um item da lista de 'cumprimentos
print(choice(cumprimentos))
print("De nada!")

#Etapa 1, é legal ser legal!

from random import*
print("Gerador de cumprimentos")
print("-"*10)

adjetivos = ["maravilhoso","acima da média","excelente"]
hobbies =["andar de bicicleta","programar","fazer chá"]

nome = input("Qual é o seu nome?:")
print("Aqui está o seu cumprimento", nome , ":")

print(nome, "você é" ,choice(adjetivos), "em",choice(hobbies))
print("De nada!")