from datetime import datetime
import Cliente, Conta

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._trensacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )
        
    def exebir_estrato():
        cpf = input("Informe o CPF do cliente: ")
        cliente = Cliente.filtrar_cliente(cpf, clientes)
        
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
                extrato +=f"\n{transacao['tipo']}:\n\tR$
                {transacao['valor']:.2f}"
        
        print(extrato)
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("|n########################")
        