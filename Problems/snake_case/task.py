camel_case = input()
count = 0

for i in camel_case:
    if i.isupper():
        camel_case = camel_case.replace(i, '_' + i.lower())
    count += 1

print(camel_case)
