# print debugging:
# this is to identify which line is being printed or not printed.

i = 10
count = 1
print("Starting the first loop...")
while count < i:
    count += 1
print(count)
print("Finishing the first loop.")

print("Starting the second loop...")
while count > 0:
    count -= 1
print(count)
print("Finishing the second loop.")
