import string

f= open("attacco/file.txt","w")
lettere = string.ascii_letters + "0123456789"

for i1 in range(len(lettere)):
    for i2 in range(len(lettere)):
        for i3 in range(len(lettere)):
            f.write(f"{lettere[i1]}{lettere[i2]}{lettere[i3]}\n")

print("Finito")
f.close()