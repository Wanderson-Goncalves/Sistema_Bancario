from Transacao import Transacao

class Cliente:
    def __init__(self, endereco):
        self.enderco = endereco
        self.contas = []
    
    def filtrar_cliente(cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self,conta):
        self.contas.append(conta)
        
    def criar_cliente(clientes):
        from Pessoa_Fisica import Pessoa_Fisica
        cpf = input("Informe o CPF (somente número): ")
        cliente = Cliente.filtrar_cliente(cpf, clientes)
        
        if cliente:
            print("\n### Já existe cliente com esse CPF! ### ")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado: )")
        
        cliente = Pessoa_Fisica(nome = nome, 
                                data_nascimento = data_nascimento,
                                cpf = cpf,
                                endereco = endereco)
        
        clientes.append(cliente)
        
        print("\n### Cliente criado com sucesso! ###")
        
    