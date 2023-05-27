# with open('email.txt', 'r') as arquivo:
#     email = arquivo.read()
# print(email)

# with open('mensagem.txt', 'r') as msg:
#     text = msg.readlines()

# for line in text:
#     if 'tiverem' in line:
#         print(line)

senhas = ['Diogo','Junin','Alana','Julia','Gabi']
with open('senha_nova.txt', 'a') as senhanova:
    for i in senhas:
        senhanova.write(i + '\n')
