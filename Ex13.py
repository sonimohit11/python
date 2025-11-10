# a. Count lines, words, and characters in example.txt

filename = "ict.txt"

with open(filename, 'r') as file:
    lines = file.readlines()
n_l = len(lines)
n_w = sum(len(line.split()) for line in lines)
n_c = sum(len(line) for line in lines)

print(f"Num of lines: {n_l}")
print(f"Num of words: {n_w}")
print(f"Num of characters: {n_c}")

# b. Read a text file line by line and store in a list

filename = "ict.txt"

lines_list = []
with open(filename, 'r') as file:
    for line in file:
        lines_list.append(line.strip()) 

print("List of lines:")
print(lines_list)


# c. Read data from a CSV file and print each row

import csv

filename = "data.csv"

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


# d. Merge two text files into a third file

file1 = "ict.txt"
file2 = "ict1.txt"
merged_f = "merged.txt"

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged_f, 'w') as mf:
    mf.write(f1.read())
    mf.write(f2.read())

print("Files merged")