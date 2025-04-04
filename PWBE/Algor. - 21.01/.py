# LEIA E SOME DOIS NUMEROS
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
soma = num1+num2

print(soma)

# LER ANO DE NASCIMENTO, E PRINT IDADE EM 
ano = int(input("Digite seu Ano de nascimento: "))

print(f"Você vai ter {2025-ano} anos em 2025!")






# LER IMPAR OU PAR
num = int(input("Digite um número: "))

print ('O número é par' if (num%2)==0 else 'O número é ímpar')

# LER NOTA
nota = 0
for i in range(5):
    notaa = int(input(f"Digite a nota {i+1}: "))
    nota += notaa

media = nota/5

if media >= 5:
    resultado = "Aprovado"
elif media >= 2.5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print (resultado)








# DE 0 A X
num = int(input("Digite um número: "))
contador = 0
while contador <= num:
    print(contador)
    contador +=1

# NUM POSITIVO, MAIOR
num = int(input("Digite um número: "))
maiorNum = 0
while num > 0:
    num = int(input("Digite um número: "))
    if maiorNum < num:
        maiorNum = num

print(maiorNum)






# INVERTER STRING
def reverse(text):
    inv = ""
    for i in text:
        inv = i + inv
    return inv

string = input("Digite uma palavra: ")
inv = reverse(string)
print(f"String original: {string}")
print(f"String invertida: {inv}")

# CONTA LETRAS 
def count(word):
    caract= {}
    for i in word:
        if i in caract:
            caract[i] += 1
        else:
            caract[i] = 1
    return caract

word = input("Digite uma palavra: ")
dicionario = count(word)
print(f"Contagem de caracteres: {dicionario}")
