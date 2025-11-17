v1 = list(map(float, input("Enter the first vector : ").split()))
v2 = list(map(float, input("Enter the second vector : ").split()))
if len(v1) != len(v2):
    print("Error: Vectors must be of the same length.")
else:
    dotproduct = sum(a * b for a, b in zip(v1, v2))
    print("Dot Product:", dotproduct)

#python

