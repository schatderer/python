url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# Separa base e parâmetros da url:
url_base, url_parametros = url.split("?")
print(url_parametros)

# Busca o valor de um parâmetro:
parametro_busca = "moedaDestino"                  # "moedaOrigem", "moedaDestino" ou "quantidade"
lista_parametros = url_parametros.split("&")

for parametro in lista_parametros:
    nome, valor = parametro.split("=")
    if nome == parametro_busca:
        print(valor)

# parametro_busca = "quantidade"
# indice_parametro = url_parametros.find(parametro_busca)
# indice_valor = indice_parametro + len(parametro_busca) + 1
# indice_e_comercial = url_parametros.find("&", indice_valor)
#
# if indice_e_comercial == -1:
#     valor = url_parametros[indice_valor:]
# else:
#     valor = url_parametros[indice_valor:indice_e_comercial]
#
# print(valor)
