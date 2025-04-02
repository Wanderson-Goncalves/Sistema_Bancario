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
                "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S")
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
        # TODO: atualizar a implementação para utilizar o gerador definido em Historico
        transacoes = conta.historico.gerar_relatorio()
        tem_transacao = False
        
        extrato = ""
        if not transacoes:
            extrato = "Não foram realizadas movimentações."
        
        for transacao in transacoes:
            tem_transacao = True
            extrato +=f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
        
        print(extrato)
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("\n########################")
        
    
    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        
        for transacao in transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y  %H:%M:%S").date()
            
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes
        
    def gerar_relatorio(self, tipo_transacao = None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao
   
        