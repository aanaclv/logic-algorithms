n = int(input("How many numbers will you enter: "))
vector = []
for i in range(n):
    value = int(input("Enter a number: "))
    vector.append(value)

max = max(vector)
print(f"highest value: {max}")

position = vector.index(max(vector))
print(f"highest-value position: {position}")