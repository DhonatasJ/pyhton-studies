carne = input("Qual a carne você deseja? ");
kg = float(input("Quantos quilos? "));
pgtox = input("Qual seria a forma de pagamento? ");
pgto = pgtox.upper();

def escolheCarne(carne, kg):
    fileDuploL5, fileDuploG5 = 4.9, 5.8;
    alcatraL5, alcatraG5 = 5.9, 6.8;
    picanhaL5, picanhaG5 = 6.9, 7.8;
    if carne == "file duplo" and kg <= 5:
        x = fileDuploL5
        return x
    elif carne == "file duplo" and kg > 5:
        x = fileDuploG5
        return x
    elif carne == "alcatra" and kg <= 5:
        x = alcatraL5
        return x
    elif carne == "alcatra" and kg > 5:
        x = alcatraG5
        return x
    elif carne == "picanha" and kg <= 5:
        x = picanhaL5
        return x
    elif carne == "picanha" and kg > 5:
        x = picanhaG5
        return x
vlrBruto = escolheCarne(carne, kg) * kg;
desconto = ((vlrBruto / 100) * 10);

if pgto == "cartao tabajara":
    vlrLiquido = vlrBruto - desconto
    desconto = ((vlrBruto / 100) * 10)
else:
    vlrLiquido = vlrBruto
    desconto = 0;

print(f"-------NOTA FISCAL-------- \n Tipo: {carne}\n Quantidade: {kg:.2f}KG\n Preço Total: R${vlrBruto:.2f}\n "
      f"Tipo de Pagamento: {pgto}\n Valor do Desconto: R${desconto:.2f} \n Valor a Pagar: R${vlrLiquido:.2f}")

