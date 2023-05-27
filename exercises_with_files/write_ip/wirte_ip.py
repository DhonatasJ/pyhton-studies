# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4

# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256
 
all_ips = ['200.135.80.9','192.168.1.1','8.35.67.74','257.32.4.5','85.345.1.2','1.2.3.4','9.8.234.5','192.168.0.256']
valid_ips = ['200.135.80.9','192.168.1.1','8.35.67.74','1.2.3.4']
invalid_ips = ['257.32.4.5','85.345.1.2','9.8.234.5','192.168.0.256']
with open('all_ips', 'w') as w_all_ips:
    for i in all_ips:
        w_all_ips.write(i + '\n')
    
with open('vaid_ips', 'w') as w_valid_ips:
    for vIp in all_ips:
        if vIp in valid_ips:
            w_valid_ips.write(vIp + '\n')

with open('invalid_ips', 'w') as w_invalid_ip:
    for i_ip in all_ips:
        if i_ip in invalid_ips:
            w_invalid_ip.write(i_ip + '\n')
            