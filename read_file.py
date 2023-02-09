file1 = open('text01.txt', 'r')
lines = file1.readlines()
file1.close()
print(lines)

with open('text01.txt', 'r') as textfile:
    lines = textfile.readline()
print(lines)

# Iterate through lines
# with open('text01.txt', 'r') as textfile:
#     for line in textfile:
#         print(line)
