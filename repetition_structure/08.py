nums = [];
for i in range(1,6):
    x = float(input(f"Enter a {i}º number: "))
    nums.append(x)
z = sum(nums) / len(nums)

print(z)