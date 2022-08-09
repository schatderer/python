# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = " "

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa base e parâmetros da URL
url_base, url_parametros = url.split("?")
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = "moedaDestino"                  # "moedaOrigem", "moedaDestino" ou "quantidade"
lista_parametros = url_parametros.split("&")

for parametro in lista_parametros:
    nome, valor = parametro.split("=")
    if nome == parametro_busca:
        print(valor)
