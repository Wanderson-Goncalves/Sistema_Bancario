from Transacao import Transacao
from Cliente_modulo import Cliente
from Conta import Conta
from log_transacao import log_transacao


class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor) 
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
    @log_transacao       
    def sacar(clientes):
        cpf = input("Informe o CPF do cliente: ")
        cliente  = Cliente.filtrar_cliente(cpf, clientes)
        
        if not cliente:
            print("\n### Cliente não encontrado! ###")
            return
        
        valor = float(input("Informe o valor do saque: "))
        transacao = Saque(valor)
        
        conta = Conta.recuperar_conta_cliente(cliente)
        if not conta:
            return
        
        cliente.realizar_transacao(conta, transacao)