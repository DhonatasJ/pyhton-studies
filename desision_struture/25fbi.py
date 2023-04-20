print("Please, just answear the questions using Y to \"yes\" or N to \"not\"");

one = input("Did you call a victim? ");
two = input("Were you without a local crime? ");
three = input("Do you live near the victim? ");
four = input("Do you owed money to the victim? ");
five = input("Have you worked with a victim? ");
aswr = [one, two, three, four, five];
y = 0
n = 0
for x in aswr:
    if x == "Y":
        y += 1;
    elif x == "N":
        n += 1;

if y == 2:
    situation = "suspicious";
elif y > 2 and y < 5:
    situation = "complicit";
elif y == 5:
    situation = "killer";
elif y < 2:
    situation = "innocent";
else:
    situation = "Invalid answear, please try again..."
print(situation);
