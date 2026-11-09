'''
Write a program that reads N real numbers and stores them in a vector. Then, display on the screen
the largest number in the vector (assuming there are no ties). Also display the position of the largest element,
considering the first position to be 0 (zero).
'''

n = int(input("How many numbers will you enter: "))
vector = []
for i in range(n):
    value = int(input("Enter a number: "))
    vector.append(value)

max = max(vector)
print(f"highest value: {max}")

position = vector.index(max(vector))
print(f"highest-value position: {position}")