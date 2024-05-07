def kabisat (d):
    if d % 400 == 0:
        return True
    if d % 100 == 0:
        return False
    if d % 4  == 0:
        return True
    else:
       return False
tahun =int(input("Masukan tahun : "))
print("")

if kabisat(tahun):
    print (tahun, "ini adalah tahun kabisat")
else:
    print(tahun, "ini adalah bukan tahun kabisat")


print("===========")
print("AINUR ROFIQ")
print("===========")