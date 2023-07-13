s = float(input('Digite o valor do salário do Funcionario: '))
a = int(input('Digite o valor em % do aumento do Funcionario: '))

s = float((a/100+1)*s)

print('O valor do novo salário é de: R${:.2f}'.format(s))
