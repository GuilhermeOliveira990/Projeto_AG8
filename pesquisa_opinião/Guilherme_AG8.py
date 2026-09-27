cont_excelente  = 0
cont_ruim = 0
cont_bom = 0
for i in range(1, 4):
    nome = input('Qual é o seu nome? ')
    idade = int(input('Qual é a sua idade? '))
    opnião = int(input('Qual é a sua opnião sobre a entrevista? digite 1: EXCELENTE. 2: BOM. 3: RUIM. '))
    if opnião == 1:
        cont_excelente += 1
    elif opnião == 2:
        cont_bom += 1
    elif opnião == 3:
        cont_ruim += 1
print('Quantidade de Excelentes:', cont_excelente,'Quantidade de Boms:', cont_bom,'. Quantidade de Ruims:', cont_ruim)