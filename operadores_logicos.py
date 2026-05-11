#operador E (and)
#saldo>= and saque<= limite
# todos tem que estar em true para que ele informe se é verdadeiro
# operador OU (or)
# saldo >= saque or saque<=limite(uma das condições precisa ser verdadeira ele afirma como true)
# operador negação(ele confirma se utilizar not exemplo ao comparar um número é não ser maior ele vai afirmar true porque ele é um not)
# not 1000>1500
# >>> true
# not contatos_emergencia
#>>> true
#not 'saque1500;'
#>>> false
#not ' '
#>>> true
# parênteses
#tabela para lembra
# true and true=true
# true and false= false
# true or false= true
# true or true= true
# false or false= false

saldo=1000
saque=250
limite=200
conta_especial=True
exp=saldo >= saque and saque <= limite or conta_especial and saldo>= saque
print(exp)
exp2=( saldo >= saque and saque <= limite) or (conta_especial and saldo>= saque)
print(exp2)