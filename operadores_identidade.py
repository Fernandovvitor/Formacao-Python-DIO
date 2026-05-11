# a função is ela compara se o objeto a  tem o mesmo objeto na outra variavel
# a função is not para negar se as variaveis ocupam o mesmo espaço de memoria

curso='curso de python'
nome_curso = curso
saldo, limite  =200,200
curso is nome_curso

curso is not nome_curso

saldo is limite

saldo=1000
limite=500
print(saldo is limite)
print(saldo is not limite)