class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} like(s)'

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} like(s)'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} like(s)'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):        # __getitem__ é um  "método dunder" que serve para tornar um objeto
        return self._programas[item]    # iterável, ou seja, para que consigamos percorrê-lo item por item

    def __len__(self):
        return len(self._programas)


top_gun = Filme('Top Gun: Maverick', 2022, 130)
the_office = Serie('the office', 2005, 9)
goonies = Filme('the goonies', 1985, 114)
modern_family = Serie('modern family', 2009, 11)
friends = Serie('Friends', 1994, 10)

top_gun.dar_like()
top_gun.dar_like()
the_office.dar_like()
the_office.dar_like()
goonies.dar_like()
the_office.dar_like()
the_office.dar_like()
modern_family.dar_like()
modern_family.dar_like()

filmes_e_series = [top_gun, the_office, modern_family, goonies]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)} programas')

print(f'"{friends.nome}" está na playlist? {"Sim" if friends in playlist_fim_de_semana else "Não"}')
print(f'"{top_gun.nome}" está na playlist? {"Sim" if top_gun in playlist_fim_de_semana else "Não"}')

for programa in playlist_fim_de_semana:
    print(programa)
