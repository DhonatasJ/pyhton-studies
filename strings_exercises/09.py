cpf = input("Insira o CPF no formato \"xxx.xxx.xxx-xx\": ")

def valida_cpf(cpf):    
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False  
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto >= 10 else resto
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10)) 
    resto = (soma * 10) % 11
    digito2 = 0 if resto >= 10 else resto
    
    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        return False
    return True
    
resultado = valida_cpf(cpf)
if resultado:
    print("CPF VÁLIDO!")
else:
    print("CPF INVÁLIDO!")
