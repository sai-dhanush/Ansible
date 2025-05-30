user_array= []

size = int(input("How many numbers you wana add: "))

for i in range(size):
    num = int(input(f"Enter value: {i+1} "))
    user_array.append(num)

print(user_array)

for num in user_array:
    if num%2==0:
        print(f"{num} is Even number")
    else:
        print(f"{num} is odd number")