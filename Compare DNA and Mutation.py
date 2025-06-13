#take two strings and compare it and print the positions(indices) where the sequence differ.
seq1 = input("Enter the First Sequence: ")
seq2 = input("Enter the First Sequence: ")
mutation_points = []
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        mutation_points.append(i)
print("Positions Differ in : ",mutation_points)