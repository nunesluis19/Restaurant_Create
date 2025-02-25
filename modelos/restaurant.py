from modelos.Avaliação import Avaliacao

class Restaurante:
    # Lista para armazenar todos os restaurantes criados
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa um restaurante com nome, categoria e estado inativo.
        Também adiciona o restaurante à lista de restaurantes.
        """
        self._nome = nome.title()  # Formata o nome para ter a primeira letra maiúscula
        self._categoria = categoria.upper()  # Formata a categoria para letras maiúsculas
        self._ativo = False  # Estado inicial do restaurante
        self._avaliacao = []  # Lista de avaliações do restaurante
        Restaurante.restaurantes.append(self)  # Adiciona o restaurante à lista de restaurantes

    def __str__(self):
        """
        Retorna uma string representando o restaurante no formato: Nome | Categoria.
        """
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        """
        Lista todos os restaurantes cadastrados, mostrando nome, categoria, média de avaliações e status.
        """
        print(f"{"nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        """
        Retorna um símbolo indicando se o restaurante está ativo ou não.
        """
        return "\u2716" if self._ativo else "\u2610"  # ⌧ para ativo, ☐ para inativo

    def alternar_estado(self):
        """
        Alterna o estado do restaurante entre ativo e inativo.
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Adiciona uma avaliação ao restaurante, desde que a nota esteja no intervalo de 0 a 5.
        """
        if nota <= 5:
            avaliacao = Avaliacao(cliente, nota)  # Cria uma nova instância de Avaliacao
            self._avaliacao.append(avaliacao)  # Adiciona a avaliação à lista de avaliações
       
    @property
    def media_avaliacoes(self):
        """
        Calcula e retorna a média das avaliações do restaurante.
        Se não houver avaliações, retorna "Sem avaliação".
        """
        if not self._avaliacao:
            return "Sem avaliação"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)  # Arredonda para uma casa decimal
        return media
