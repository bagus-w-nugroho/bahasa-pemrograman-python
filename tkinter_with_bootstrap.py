import tkinter as tk
from tkinter.messagebox import showinfo
import ttkbootstrap as ttkb

window = ttkb.Window(themename="morph")  
window.geometry("800x600")
window.title("APLIKASI PENDAFTARAN MAHASISWA BARU")
window.resizable(False, False)

#frame area kerja
input_frame = ttkb.Frame(window)
input_frame.pack(padx=50, pady=10, fill="x", expand=True)

# Label untuk Nama Depan
nama_depan_label = ttkb.Label(input_frame, text="MASUKKAN NAMA DEPAN")
nama_depan_label.pack(padx=20, pady=5, fill="x", expand=True)

# ini untuk deklarasi input user dengan nama variabel NAMA_DEPAN
NAMA_DEPAN = ttkb.StringVar()
nama_depan_entry = ttkb.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=30, pady=5, fill="x", expand=True)

# Label untuk Nama belakang
nama_belakang_label = ttkb.Label(input_frame, text="MASUKKAN NAMA BELAKANG")
nama_belakang_label.pack(padx=20, pady=5, fill="x", expand=True)

# ini untuk deklarasi input user dengan variabel NAMA_BELAKANG
NAMA_BELAKANG = ttkb.StringVar()
nama_belakang_entry = ttkb.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=30, pady=5, fill="x", expand=True)

# Fungsi untuk menyimpan data ke dalam file
def simpan_ke_database(NAMA_DEPAN, NAMA_BELAKANG):
    with open("data_nama.txt", "a") as file:
        file.write(f"{NAMA_DEPAN} {NAMA_BELAKANG}\n")

#fungsi saat tombol Simpan ditekan keluar peringatan "Data berhasil disimpan!" dan menjalankan fungsi simpan_ke_database
def tombol_klik_simpan():
    pesan = f"Data berhasil disimpan!"
    showinfo(title="Informasi", message=pesan)
    simpan_ke_database(NAMA_DEPAN.get(), NAMA_BELAKANG.get())

#tombol simpan
tombol_simpan = ttkb.Button(input_frame, text="SIMPAN", command=tombol_klik_simpan)
tombol_simpan.pack(padx=250, pady=15, fill="x", expand=True)
                            
#agar aplikasi tetap berjalan
window.mainloop()













# window.resizable(False, False)

# # Frame untuk input
# input_frame = ttkb.Frame(window)

# input_frame.pack(padx=50, pady=10, fill="x", expand=True)

# # Label dan entry untuk Nama Depan
# nama_depan_label = ttkb.Label(input_frame, text="MASUKKAN NAMA DEPAN", font=("Arial", 12))
# nama_depan_label.pack(padx=20, pady=5, fill="x", expand=True)

# NAMA_DEPAN = ttkb.StringVar()
# nama_depan_entry = ttkb.Entry(input_frame, textvariable=NAMA_DEPAN, font=("Arial", 12))
# nama_depan_entry.pack(padx=20, pady=5, fill="x", expand=True)

# # Label dan entry untuk Nama Belakang
# nama_belakang_label = ttkb.Label(input_frame, text="MASUKKAN NAMA BELAKANG", font=("Arial", 12))
# nama_belakang_label.pack(padx=20, pady=5, fill="x", expand=True)

# NAMA_BELAKANG = ttkb.StringVar()
# nama_belakang_entry = ttkb.Entry(input_frame, textvariable=NAMA_BELAKANG, font=("Arial", 12))
# nama_belakang_entry.pack(padx=20, pady=5, fill="x", expand=True)

# # Fungsi untuk menyimpan data ke dalam file
# def simpan_ke_txt(NAMA_DEPAN, NAMA_BELAKANG):
#     with open("data_nama.txt", "a") as file:
#         file.write(f"{NAMA_DEPAN} {NAMA_BELAKANG}\n")  

# # Fungsi saat tombol Simpan ditekan
# def tombol_klik_simpan():
#     print("Nama Depan:", NAMA_DEPAN.get())
#     print("Nama Belakang:", NAMA_BELAKANG.get())
#     pesan = f"Data berhasil disimpan! {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
#     showinfo(title="Informasi", message=pesan)
#     simpan_ke_txt(NAMA_DEPAN.get(), NAMA_BELAKANG.get())

# # Tombol Simpan dengan gaya yang lebih menarik
# tombol_simpan = ttkb.Button(input_frame, text="SIMPAN", command=tombol_klik_simpan, bootstyle="primary", width=20)
# tombol_simpan.pack(padx=50, pady=15, fill="x", expand=True)

# # Menjalankan aplikasi

