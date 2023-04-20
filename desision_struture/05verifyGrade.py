firstGrade = float(input("Enter the first student's grade: "));
secondGrade = float(input("Enter the second student's grade: "));
media = (firstGrade + secondGrade) / 2;
if media < 7:
    print("Reprovado");
elif media >= 7 and media <= 9.9:
    print("Aprovado");
elif media == 10:
    print("Aprovado com Distinção");
else:
    print("Nota inválida.");

