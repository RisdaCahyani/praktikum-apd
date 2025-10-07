produk = {
    "1": {"nama": "Kopi Cappuccino", "harga": 25000},
    "2": {"nama": "Roti Gandum", "harga": 15000},
    "3": {"nama": "Jus Alpukat", "harga": 30000},
}

USERNAME_MEMBER = "risdach"
PASSWORD_MEMBER = "170207"

print("Selamat datang di Toko Cahaya!")
status_member = input("Apakah Anda member? (ya/tidak): ").lower()

is_member = (status_member == "ya")

if is_member:
    max_attempts = 3
    attempt_count = 0
    login_berhasil = False

    while attempt_count < max_attempts:
        print(f"\n--- Menu Login (Kesempatan ke-{attempt_count + 1})")
        username = input("Username: ") 
        password = input("Password: ")

        if username == USERNAME_MEMBER and password == PASSWORD_MEMBER:
            login_berhasil = True
            break
        else:
            print("Username atau password salah.")
            attempt_count += 1

    if login_berhasil:
        print("\nLogin berhasil!")

keranjang = {}
print("\n--- Menu Belanja ---")
for key, item in produk.items():
    print(f"[{key}] {item['nama']} - Rp{item['harga']}")

while True:
    pilihan = input("Pilih produk (ketik 'selesai' untuk mengakhiri): ")
    if pilihan == 'selesai':
        break
    if pilihan in produk:
        try:
            jumlah = int(input(f"Masukkan jumlah {produk[pilihan]['nama']}: "))
            if jumlah > 0:
                keranjang[pilihan] = keranjang.get(pilihan, 0) + jumlah
                print(f"{jumlah} {produk[pilihan]['nama']} ditambahkan ke keranjang.")
            else:
                print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Jumlah tidak valid. Masukkan angka.")
    else:
        print("Pilihan tidak valid.")

total_belanja = 0

while True:
    pilihan_produk = input("Pilih kode produk (atau 'selesai' untuk mengakhiri): ").lower()
    if pilihan_produk == "selesai":
        break
    
    if pilihan_produk in produk:
        try:
            jumlah = int(input(f"Berapa {produk[pilihan_produk]['nama']} yang ingin Anda beli? "))
            total_belanja += produk[pilihan_produk]['harga'] * jumlah
        except ValueError:
            print("Jumlah tidak valid. Masukkan angka.")
    else:
        print("Kode produk tidak valid.")

    total_belanja = 0
    keranjang_belanja = []

if keranjang:
    total_belanja = 0
    print("\n===============================")
    print("      STRUK BELANJA CAHAYA")
    print("===============================")
    for pilihan, jumlah in keranjang.items():
        harga_satuan = produk[pilihan]['harga']
        subtotal_produk = harga_satuan * jumlah
        total_belanja += subtotal_produk
        print(f"{produk[pilihan]['nama']} ({jumlah}x): Rp{subtotal_produk}")
    
    diskon = 0
    if is_member:
        diskon = total_belanja * 0.15
    
    total_akhir = total_belanja - diskon

    print("-------------------------------")
    print(f"Subtotal: Rp{total_belanja}")
    if is_member:
        print(f"Diskon Member (15%): Rp{int(diskon)}")
    print("===============================")
    print(f"Total Bayar: Rp{int(total_akhir)}")
    print("===============================")
    print("         TERIMA KASIH")
    print("===============================")
else:
    print("Keranjang belanja kosong.")
  
if is_member:
    diskon_persen = 0.15
    total_diskon = total_belanja * diskon_persen
    harga_setelah_diskon = total_belanja - total_diskon
    
    print(f"\n--- Ringkasan Belanja Member ---")
    print(f"Harga sebelum diskon: Rp {total_belanja:,}")
    print(f"Total diskon (15%): Rp {total_diskon:,.0f}")
    print(f"Harga setelah diskon: Rp {harga_setelah_diskon:,.0f}")
else:
    print(f"\n--- Ringkasan Belanja Non-Member ---")
    print(f"Total harga belanja: Rp {total_belanja:,}")

print("Terima kasih telah berbelanja!")