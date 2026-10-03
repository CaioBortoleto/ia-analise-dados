#Lista

#lista_de_compras = ["Maçã", "Detergente", "Arroz", ]
# print(lista_de_compras)

#Adiciona um dado ao final da lista
# lista_de_compras.append("Feijão")

#Adiciona um dado na posição desejada
#lista_de_compras.insert(1, "Sabão em pó")

#Remove um dado específico 
# lista_de_compras.remove("Arroz")

#Remove o último elemento da lista, ou pode passar o index
#lista_de_compras.pop()


# notas = [10,4,7.5,9,8,7]
# print(max(notas)) #Maior nota
# print(min(notas)) #Nota menor
# print(sum(notas)) #Soma das notas
# print(len(notas)) #Tamanho de elementos 



def mensagem_com_linha(frase):
    print("-"*len(frase))
    print(frase)
    print("-"*len(frase))
mensagem_com_linha("Bem vindo ao seu sistema de notas!")

lista_nota=[]

for _ in range(4):
    nota=float(input("Digite sua nota: "))
    lista_nota.append(nota)
print(f"\nSua maior nota é {max(lista_nota)}")
print(f"\nSua menor nota é {min(lista_nota)}")
print(f"\nA soma de todas as notas é {sum(lista_nota)}")


def media(lista_nota):
    media = sum(lista_nota) / len(lista_nota)
    if media >=6:
        return f"Sua média é {media:.2f} e você está aprovado!"
    else:
        return f"Sua média é igual a {media:.2f} e você está reprovado"
print(media(lista_nota))





# import pandas as pd
# df = pd.DataFrame(lista_nota)
# media = df[lista_nota].mean()
# print(media)

# pip3 install pandas