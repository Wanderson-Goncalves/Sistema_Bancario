from datetime import datetime
from Cliente_modulo import Cliente


class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )
        
    @staticmethod
    def exibir_extrato(cliente):
        from Conta import Conta
        cpf = input("Informe o CPF do cliente: ")
        cliente = Cliente.filtrar_cliente(cpf, cliente)
        
        if not cliente:
            print("\n### Cliente não encontrado! ###")
            return
        
        conta = Conta.recuperar_conta_cliente(cliente)
        if not conta:
                return
        
        print("\n########## EXTRATO ##########")
        transacoes = conta.historico.transacoes
        
        extrato = ""
        if not transacoes:
            extrato = "Não foram realizadas movimentações."
        
        else:
            for transacao in transacoes:
                extrato +=f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
        
        print(extrato)
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("|n########################")
        