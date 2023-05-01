# Insertion function palindromo
def functionPalindromo(palavra):
    comparador = palavra
    if palavra == palavra[::-1]:
        return "E palindromo"
    else:
        return "Não!!! e palindromo"
    
# imports locale
from Fatorial import Fatorial

x = input("Quanto tempo quer contabilizar?: ")
x = int(x)
# Insertion function timer
# 
# 
#  Insertion function fatorial
fatorial = Fatorial()
print("Fim do timer, obrigado por testar")
print("O fatorial deste numero e ",fatorial.fatorial(x))
palavra = input("Digite uma palavra para verificar se ela é palindroma ou não: ")
print(functionPalindromo(palavra))