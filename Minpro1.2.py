# Data pasien
list_pasien = [
    {
        "ID": 1,
        "data_tetap": ("Rizky", "Jl. Harapan 4", 23),
        "Penyakit": "Radang Tenggorokan",
        "Diagnosa": "Infeksi Bakteri",
        "Status": "Rawat Jalan"
    },
    {
        "ID": 2,
        "data_tetap": ("Aulia", "Jl. Kusuma 1", 25),
        "Penyakit": "Asam Lambung",
        "Diagnosa": "GERD",
        "Status": "Rawat Inap",
    },
    {
        "ID": 3,
        "data_tetap": ("Agus", "Jl. Pahlawan 6", 40),
        "Penyakit": "Hipertensi",
        "Diagnosa": "Tekanan darah ≥140/90",
        "Status": "Rawat Inap"
    }
]

# Menampilkan Semua Data Para Pasien
def Tampilkan_Semua():
    print("\nData Pasien")
    for pasien in list_pasien:
        print(f"ID  :{pasien["ID"]}, Nama   :{pasien["data_tetap"][0]}, Alamat    :{pasien["data_tetap"][1]}, Usia   :{pasien["data_tetap"][2]}, Diagnosa   :{pasien["Diagnosa"]}, Status   :{pasien["Status"]}")

# Mencari Data Pasien
def Mencari_Data():
    cari = input("Cari berdasarkan (1) Nama atau (2) ID? ")
    if cari == "1":
        nama = input("Masukkan nama pasien: ").strip()
        hasil = [p for p in list_pasien if p['data_tetap'][0].lower() == nama.lower()]
    elif cari == "2":
        id_cari = int(input("Masukkan ID pasien: "))
        hasil = [p for p in list_pasien if p['ID'] == id_cari]
    else:
        print("Pilihan tidak valid.")
        return
    if hasil:
        for pasien in hasil:
            print(f"ID: {pasien['ID']}, Nama: {pasien['data_tetap'][0]}, Alamat: {pasien['data_tetap'][1]}, Usia: {pasien['data_tetap'][2]}, Penyakit: {pasien['Penyakit']}, Diagnosa: {pasien['Diagnosa']}, Status: {pasien['Status']}")
    else:
        print("Data pasien tidak ditemukan.")


# Tambah Pasien
def Tambah_Pasien():
    id_baru = max(p["ID"] for p in list_pasien) + 1
    id_baru = 1 
    nama = (input("Nama: ")).strip()
    alamat = (input("Alamat: ")).strip()
    usia = int(input("Usia: "))
    penyakit = input("Penyakit: ").strip()
    diagnosa = input("Diagnosa: ").strip()
    status = input("Status (Rawat Jalan/Rawat Inap): ").strip()

    pasien_baru = {
        "ID": id_baru,
        "data_tetap": (nama,alamat,usia),
        "penyakit": penyakit,
        "diagnosa": diagnosa,
        "status": status 
    }
    list_pasien.append(pasien_baru)
    print("Data pasien berhasil ditambahkan.")

# Update Data Pasien
def Update_Data():
    id_update = int(input("Masukkan ID Pasien :"))
    pasien = next((p for p in list_pasien if p["ID"] == id_update), None)
    if pasien is None:
        print("Data Pasien Tidak Di Temukan")
    
    print(f"Data saat ini: Penyakit: {pasien['Penyakit']}, Diagnosa: {pasien['Diagnosa']}, Status: {pasien['Status']}")
    Penyakit_Baru = (input("Masukkan Penyakit Baru: "))
    Diagnosa_Baru = (input("Masukkan Diagnosa Baru: "))
    Status_Baru = (input("Masukkan Status Baru: "))

    if Penyakit_Baru:
        pasien["Penyakit"] = Penyakit_Baru
    if Diagnosa_Baru:
        pasien["Diagnosa"] = Diagnosa_Baru
    if Status_Baru:
        pasien["Status"] = Status_Baru
    print("Data Pasien Berhasil Di Update")

print("Menu:")
print("1. Tampilkan semua data pasien")
print("2. Cari data pasien")
print("3. Tambah data pasien")
print("4. Update data pasien")

Pilihan = (input("Pilih Menu 1-5: "))

if Pilihan == "1":
    Tampilkan_Semua()
elif Pilihan == "2":
    Mencari_Data()
elif Pilihan == "3":
    Tambah_Pasien()
elif Pilihan == "4":
    Update_Data()
else:
    print("Pilihan Tidak Valid")
