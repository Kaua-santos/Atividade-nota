class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        return self.__codigo
        return self.__titulo
        return self.__ano
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self .__disponivel == False
            print("Livro disponivel para emprestimo")
        else:
            return "Livro indisponivel para emprestimo"

    def delvolver(self):
        self.__disponivel = True
        return "livro devolvido"
    
        