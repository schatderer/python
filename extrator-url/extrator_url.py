import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.valida_url_parametros()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"URL: '{self.url}'\nBase da URL: '{self.get_url_base()}'\n" \
               f"Parâmetros da URL: '{self.get_url_parametros()}'"

    def __eq__(self, other):
        return self.url == other

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def valida_url_parametros(self):
        if self.url.find("?") == -1:
            raise ValueError("A URL não possui nenhum parâmetro.")

    def get_url_base(self):
        indice_final = self.url.find("?")
        return self.url[:indice_final]

    def get_url_parametros(self):
        indice_inicial = self.url.find("?")
        return self.url[indice_inicial + 1:]

    def get_valor_parametro(self, nome_parametro):
        indice_inicial = self.get_url_parametros().find(nome_parametro) + len(nome_parametro) + 1
        indice_final = self.get_url_parametros().find("&", indice_inicial)
        if indice_final != -1:
            valor = self.get_url_parametros()[indice_inicial:indice_final]
        else:
            valor = self.get_url_parametros()[indice_inicial:]
        return valor


string_url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
# string_url = "bytebank.com.br/cambio?a"
extrator_url = ExtratorURL(string_url)
# print(f"O tamanho da URL é: {len(extrator_url)}")
# print(extrator_url)
#
# valor_moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
# valor_moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(f"Valor do parâmetro 'moedaOrigem': {valor_moeda_origem}")
# print(f"Valor do parâmetro 'moedaDestino': {valor_moeda_destino}")
# print(f"Valor do parâmetro 'quantidade': {valor_quantidade}")

valor_dolar = 5.25
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    conversao = float(quantidade) / valor_dolar
    print(f"R$ {quantidade} = U$ {conversao:.2f}")
elif moeda_origem == "dolar" and moeda_destino == "real":
    conversao = float(quantidade) * valor_dolar
    print(f"U$ {quantidade} = R$ {conversao:.2f}")
