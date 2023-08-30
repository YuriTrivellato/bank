from conta import Conta
from banco import Banco
from cliente import Cliente

banco = Banco()

conta1 = Conta(111, '1000', "Yuri", 1000.0)
conta2 = Conta(222, '2000', "Bruna", 100.0)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

print(banco.contas['conta1'], banco.contas['conta2'])

print(f"\nConta Yuri saldo antes: {conta1.saldo}")
print(f"Conta Bruna saldo antes: {conta2.saldo}\n")

banco.transferir(111, '1000', 222, '2000', 200.0)

print(f"\nConta Yuri saldo depois: {conta1.saldo}")
print(f"Conta Bruna saldo depois: {conta2.saldo}\n")