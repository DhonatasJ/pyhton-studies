num = []
for i in range(1, 6):
    while True:
        x = int(input(f"{i}° Number "))
        if x > 1000:
            print("This number should be grander than 1000")
            continue
        num.append(x)
        break

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