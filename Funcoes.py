#AULA FUNÇOES

def Boas_vindas():
   print("Bem-vindo ao curso de Python!")

Boas_vindas()

def saudacao(nome):
   print("Olá, {}! Bem-vindo ao curso de Python!".format(nome))

saudacao("Maria")
saudacao("João")

#SOMA DE DOIS NÚMEROS

def soma(a, b):
    return a + b

resultado = soma (float(input("Digite o primeiro número: ")), 
                  float(input("Digite o segundo número: ")))
print("A soma é:", resultado)