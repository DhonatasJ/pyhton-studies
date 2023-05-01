num = []
for i in range(1, 6):
    x = int(input(f"{i}° Number "))
    num.append(x)

bnum = num[0];
for i in num:
    if i > bnum:
        bnum = i
snum = num[0]
for i in num:
    if i < snum:
        snum = i;

print(f"Sum of values is " + str(sum(num)))
print(f"Higher number is " + str(bnum))
print(f"Smaller number is " + str(snum))
