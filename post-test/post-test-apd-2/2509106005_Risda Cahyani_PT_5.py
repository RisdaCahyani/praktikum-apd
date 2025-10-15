import os

data_hewan = [
    ["id", "nama", "jenis", "pemilik"],
    ["1", "Puppy", "Anjing", "Clara"],
    ["2", "Emeng", "Kucing", "Rayn"],
    ["3", "Mikky", "Hamster", "Risda"],
    ["4", "Koci", "Kelinci", "Feby"],
    ["5", "Miko", "Marmut", "Satria"],
]

data_user = [
    ["username", "password", "role"],
    ["clara", "clara17", "admin"],
    ["rayn", "rayn555", "user"]
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def register():
    clear_terminal()
    print("=== Register Pengguna Baru ===")
    while True:
        new_user = input("Masukkan username baru: ")
        if any(user[0] == new_user for user in data_user):
            print("Username sudah ada. Silakan coba yang lain.")
        else:
            break
    new_pass = input("Masukkan password baru: ")
    data_user.append([new_user, new_pass, "user"])
    print("Pendaftaran berhasil!")
    input("Tekan Enter untuk kembali ke menu login...")

def login():
    while True:
        clear_terminal()
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        for user in data_user:
            if user[0] == username and user[1] == password:
                return user
        print("Username atau password salah. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")

def read_data():
    clear_terminal()
    print("=== Daftar Hewan Peliharaan ===")
    for row in data_hewan:
        print(f"| {row[0]:<5} | {row[1]:<10} | {row[2]:<10} | {row[3]:<10} |")
    input("Tekan Enter untuk kembali ke menu...")

def create_data():
    clear_terminal()
    print("=== Tambah Data Hewan ===")
    nama = input("Nama hewan: ")
    jenis = input("Jenis hewan: ")
    pemilik = input("Nama pemilik: ")
    new_id = str(len(data_hewan))
    data_hewan.append([new_id, nama, jenis, pemilik])
    print("Data berhasil ditambahkan.")
    input("Tekan Enter untuk kembali ke menu...")

def update_data():
    clear_terminal()
    read_data()
    print("\n=== Perbarui Data Hewan ===")
    update_id = input("Masukkan ID hewan yang ingin diperbarui: ")
    found = False
    for i in range(1, len(data_hewan)):
        if data_hewan[i][0] == update_id:
            found = True
            print("Data saat ini:", data_hewan[i])
            data_hewan[i][1] = input("Masukkan nama baru: ")
            data_hewan[i][2] = input("Masukkan jenis baru: ")
            data_hewan[i][3] = input("Masukkan nama pemilik baru: ")
            print("Data berhasil diperbarui.")
            break
    if not found:
        print("ID tidak ditemukan.")
    input("Tekan Enter untuk kembali ke menu...")

def delete_data():
    clear_terminal()
    read_data()
    print("\n=== Hapus Data Hewan ===")
    delete_id = input("Masukkan ID hewan yang ingin dihapus: ")
    found = False
    for i in range(1, len(data_hewan)):
        if data_hewan[i][0] == delete_id:
            found = True
            del data_hewan[i]
            print("Data berhasil dihapus.")
            break
    if not found:
        print("ID tidak ditemukan.")
    input("Tekan Enter untuk kembali ke menu...")

def user_menu():
    while True:
        clear_terminal()
        print("=== Menu Pengguna ===")
        print("1. Lihat Data Hewan")
        print("2. Logout")
        choice = input("Pilih menu: ")
        if choice == "1":
            read_data()
        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

def admin_menu():
    while True:
        clear_terminal()
        print("=== Menu Admin ===")
        print("1. Lihat Data Hewan")
        print("2. Tambah Data Hewan")
        print("3. Perbarui Data Hewan")
        print("4. Hapus Data Hewan")
        print("5. Logout")
        choice = input("Pilih menu: ")
        if choice == "1":
            read_data()
        elif choice == "2":
            create_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

while True:
    clear_terminal()
    print("=== Aplikasi Manajemen Data Hewan Peliharaan ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    main_choice = input("Pilih menu: ")
    
    if main_choice == "1":
        logged_in_user = login()
        if logged_in_user:
            if logged_in_user[2] == "admin":
                admin_menu()
            else:
                user_menu()
    elif main_choice == "2":
        register()
    elif main_choice == "3":
        break
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")

print("Terima kasih telah menggunakan aplikasi ini!")