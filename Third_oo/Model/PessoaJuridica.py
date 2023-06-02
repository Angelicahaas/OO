from Usuario import Usuario

class PessoaJuridica(Usuario):
    
    def __init__(self, nome: str, endereco: str, telefone: int, senha: str, cnpj: str, saldo: int, historico: int, pagamento: int ):
     super().__init__(nome, endereco, telefone, senha)
     self.__cnpj = cnpj
     self.__saldo = saldo
     self.__historico = historico
     self.__pagamento = pagamento
