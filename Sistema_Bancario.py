import textwrap
import Cliente, Conta, Deposito, Historico, Pessoa_Fisica, Saque, Transacao


def menu():
    menu = """\n
    ========== Menu ==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tMovo usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))






def main():
    clientes = []
    contas =[]
    
    while True:
        opcao = menu()
        
        if opcao =="d":
            Deposito.depositar(clientes)
            
        elif opcao == "s":
            Saque.sacar(clientes)
        
        elif opcao == "e":
            Historico.exibir_extrato(clientes)
            
        elif opcao == "nu":
            Cliente.criar_clientes(clientes)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            Conta.criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "lc":
            Conta.listar_contas(contas)
            
        elif opcao == "q":
            break
        
        else:
            print("\n@@@ Operação invália, por favor selecione novamente a operação desejada. @@@")
            