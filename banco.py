from conta import Conta

class Banco:

    def __init__(self):
        
        self.contas = {}

    def adicionar_conta(self, conta):
        contagem = len(self.contas) + 1
        if len(str(conta.agencia)) != 3:
            print("Agencia da conta incorreta, passe uma conta de 3 digitos")
        elif len(str(conta.numero)) != 4:
            print("Numero da conta incorreta, passe uma conta de 4 digitos")
        else:
            self.contas[f'conta{contagem}'] = conta

    def encontrar_conta(self, agencia, numero):
        for chave, conta in self.contas.items():
            if conta.agencia == agencia and conta.numero == numero:
                return chave
        return None

            
    def transferir(self, origem_agencia, origem_numero, destino_agencia, destino_numero, valor):
        chave_conta_origem = self.encontrar_conta(origem_agencia, origem_numero)
        chave_conta_destino = self.encontrar_conta(destino_agencia, destino_numero)

        if chave_conta_origem and chave_conta_destino:
            conta_origem = self.contas[chave_conta_origem]
            conta_destino = self.contas[chave_conta_destino]

            valor_sacado = conta_origem.sacar(valor)

            if valor_sacado > 0:
                conta_destino.depositar(valor_sacado)
                print(f"Transferência efetuada com sucesso. Valor da transferência: {valor}\n")
                print(f"Seu novo saldo é: {conta_origem.extrato()}")
            else:
                print("Transferência falhou devido a saldo insuficiente!")
        elif not chave_conta_origem:
            print("Conta origem não encontrada!")
        elif not chave_conta_destino:
            print("Conta destino não encontrada!")