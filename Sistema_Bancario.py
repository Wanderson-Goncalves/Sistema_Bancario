import textwrap
from Cliente_modulo import Cliente
from Conta import Conta
from Deposito import Deposito
from Historico import Historico
from Saque import Saque




def menu():
    menu = """\n
    ========== Menu ==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
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
            Cliente.criar_cliente(clientes)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            Conta.criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "lc":
            Conta.listar_contas(contas)
            
        elif opcao == "q":
            break
        
        else:
            print("\n@@@ Operação invália, por favor selecione novamente a operação desejada. @@@")
            
            
            
if __name__ == "__main__":
    main()

            