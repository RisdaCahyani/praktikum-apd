nama = input("Masukkan nama pasien: ")
tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))

beratIdeal = tinggi - 100

statusList = ["Berat Badan Normal", "Kelebihan Berat Badan"]
isKelebihan = berat > beratIdeal
status = statusList[int(isKelebihan)]

print("--------------------------------------------------------------")
print("|         HASIL CEK BERAT BADAN                              |")
print("--------------------------------------------------------------")
print(f"| Nama Pasien       : {nama:<40}                            |")                         
print(f"| Tinggi Badan      : {tinggi} cm{' ' * 31}                 |")
print(f"| Berat Badan       : {berat} kg{' ' * 31}                  |")
print(f"| Berat Ideal       : {beratIdeal} kg{' ' * 31}             |")
print(f"| Status            : {status:<31}                          |")
print("--------------------------------------------------------------")
