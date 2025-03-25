import textwrap
from Historico import Historico
from Cliente_modulo import Cliente 


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "1a2b"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldp suficiente. @@@")
        
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
        
        else:
            print("\n@@@ Operação falhou! O valor informadoi é inválido. @@@")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
         self._saldo += valor
         print("\n=== Depósirto realizado com sucesso! ===")
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        
        return True
    
    def recuperar_conta_cliente(cliente):
        if not cliente.contas:
            print("\n@@@ Cliente não possui conta! @@@")
            return
    
        return cliente.contas[0]
    
    def criar_conta(numero_conta, clientes, contas):
        from Conta_Corrente import ContaCorrente
        cpf = input("\nInforme o CPF do cliente: ")
        cliente = Cliente.filtrar_cliente(cpf, clientes)
        
        if not cliente:
            print("\n### Cliente não encontrado, fluxo de criação de conta encerrrado! ####")
            return
        
        conta = ContaCorrente.nova_conta(cliente, numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)
        
        print("\n### Conta criada com sucesso ###")
    
        
    def listar_contas(contas):
        for conta in contas:
            print("=" *100)
            print(textwrap.dedent(str(conta)))

        
