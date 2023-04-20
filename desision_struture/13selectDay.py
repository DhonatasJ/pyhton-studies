day = int(input("Enter some day of week, only use upper case: "));
match day:
    case 1:
        print("Domingo");
    case 2:
        print("Segunda");
    case 3:
        print("Terça");
    case 4:
        print("Quarta");
    case 5:
        print("Quinta");
    case 6:
        print("Sexta");
    case 7:
        print("Sábado");
    case _:
        print("Dia inválido");