
liczby: str = "1,23,41,2141341,4,424"
# liczby: str = input("Wpisz liczby oddzielone ,")
lislib = liczby.split(",")
max = int(lislib[0])
min = int(lislib[0])
for i in range(0, len(lislib)):
    if max < int(lislib[i]): max = int(lislib[i])
    if min > int(lislib[i]): min = int(lislib[i])

print(max, min)
