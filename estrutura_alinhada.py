conta_normal =False
conta_universitaria=False
saldo = 2000
saque = 2500
cheque_especial= 450

if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('saque realizado com uso do cheque especial')
    else: 
        print('não foi possível realizar o saque')
elif conta_universitaria:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    else:
        print( 'saldo insuficiente')
else:
    print(' não reconheceu esse seu tipo de conta, entre em contato com o seu gerente')

