x = float(input("Enter the first grade: "));
y = float(input("Enter the second grade: "));
media = (x + y) / 2;
concept = "";
situation = "";
if media >= 9 and media <= 10:
    concept = "A";
elif media >= 7.5 and media < 9:
    concept = "B";
elif media >= 6 and media < 7.5:
    concept = "C";
elif media >= 4 and media < 6:
    concept = "D";
elif media < 4 and media >= 0:
    concept = "E"
else:
    concept = "INVALID"
if concept == "A" or "B" or "C":
    situation = "APPROVED"
elif concept == "D" or "E":
    situation = "DISAPPROVED"
else:
    situation = "INVALID, please try again."

print("You media is " + str(media) + " with the concept " + str(concept) + " and situation " + str(situation))