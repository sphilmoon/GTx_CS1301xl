# scope debugging: a bundle file such as the grades variable.

grades = [100, 96, 94, 91, 90, 88, 85, 82]
sum = 0
count = 0

for grade in grades:
    count += 1
    sum += grade
    print("Current sum: ", sum)
print(sum/count)
