from modelos.restaurant import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_praca.receber_avaliacao("Gui", 10)
restaurante_praca.receber_avaliacao("Lais", 5)
restaurante_praca.receber_avaliacao("Emy", 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()