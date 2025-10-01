produk = {
    "1": {"nama": "Kopi Cappuccino", "harga": 25000},
    "2": {"nama": "Roti Gandum", "harga": 15000},
    "3": {"nama": "Jus Alpukat", "harga": 30000},
    "4": {"nama": "Croissant Keju", "harga": 20000}
}

USERNAME_MEMBER = "risdach"
PASSWORD_MEMBER = "170207"

print("Selamat datang di Toko Kami!")

status_member = input("Apakah Anda member? (ya/tidak): ").lower()

is_member = (status_member == "ya")

if is_member:
    print("\n--- Menu Login ---")
    username = input("Username: ")
    password = input("Password: ")

    
    login_berhasil = (username == USERNAME_MEMBER and password == PASSWORD_MEMBER)

    if not login_berhasil:
        print("Login gagal. Program berakhir.")
        exit()
    print("Login berhasil!")

print("\n--- Menu Belanja ---")
for kode, detail in produk.items():
    print(f"{kode}. {detail['nama']} - Rp {detail['harga']:,}")

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