import requests

cep = input("Digite seu cep: ") #Pede um cep ao usuario
url = f"https://viacep.com.br/ws/{cep}/json/" # Faz com que o cep buscado seja o mesmo que o requisitado para o usuario

dados = requests.get(url) #Faz a consulta, retorna 200 se a requisição funcionar
resposta = dados.json() #Trata os dados, tornando - os para um dicionario

print(resposta) #Printa o dicionario com os dados tratados
print(f"Você mora na {resposta["logradouro"]}, no bairro {resposta["bairro"]}, e na cidade de {resposta["localidade"]}" )