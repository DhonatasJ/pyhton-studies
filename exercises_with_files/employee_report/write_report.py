# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
emp = {}

def gera_user(emp):
    while True:
        print("Digite o nome \"FIM\", para finalizar a inserção de dados!")
        nome = input("Insira o nome do funcionario: ")
        if nome == 'FIM':
            break    
        bit = int(input("Insira a quantidade de bit que o usuario acima esta utilizando: "))
        emp[nome] = bit
gera_user(emp)

my_id = []
user = []
megabytes = []
porcent = []

def infos_of_table(emp, my_id, user, megabytes, porcent):
    for i in range(len(emp)):
        my_id.append(i+1)

    for nome in emp:
        user.append(nome.capitalize())

    for bit in emp.values():
        to_megabyte = bit * 0.000001
        megabytes.append(round(to_megabyte,2))

    for qtd in megabytes:
        p = qtd / sum(megabytes) * 100
        porcent.append(round(p,2))

infos_of_table(emp, my_id, user, megabytes, porcent)

def generate_table(my_id, user, megabytes, porcent):
    with open('relatorio.txt', 'w') as create_table:
        create_table.write('ACME Inc.               Uso do espaço em disco pelos usuários' + "\n" + '------------------------------------------------------------------' +
                            "\n" 'Nr.  Usuário         Espaço utilizado     % de uso\n')
        for i in range(len(emp)):
            create_table.write(f"{my_id[i]:<5}"  + f"{user[i]:<19}" + f"{megabytes[i]:<5}MB           " + f"{porcent[i]:<5}%\n")

        create_table.write(f"\nEspaço total ocupado: {sum(megabytes):.2f}MB\n")
        create_table.write(f"Espaço médio ocupado: {sum(megabytes) / len(megabytes):.2f}")
generate_table(my_id, user, megabytes, porcent)
