address = input("Antre adrès IP a ==> ")
lis = address.split(".")

port = 0
for code in lis:
    for i in range(len(code)):
        port += int(code[i])

first_digit = int(lis[0][0])
print(f"Pòt ki ouvri a se {port*first_digit}")
