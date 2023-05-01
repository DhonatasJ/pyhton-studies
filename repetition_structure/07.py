nums = [];
for i in range(5):
    num = float(input(f"Insira o {i+1}º numero: "));
    nums.append(num)

maior = nums[0];

for num in nums:
    if num > maior:
        maior = num;

print(maior)