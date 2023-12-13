from PIL import Image # Python Imaging Library

# Membuka Gambar Background Dengan Path File
background_image = Image.open("C:/Users/User/OneDrive/Dokumen/SYSTEM 56/KELAS A/TUGAS KULIAH SEMESTER 5/Pemograman Fungsional/Praktikum/Latihan/Modul 6/Kegiatan2/Background/UMM.jpg")  

# Membuka Gambar Overlay Dengan Path File
overlay_image = Image.open("C:/Users/User/OneDrive/Dokumen/SYSTEM 56/KELAS A/TUGAS KULIAH SEMESTER 5/Pemograman Fungsional/Praktikum/Latihan/Modul 6/Kegiatan2/Overlay/Logo.png")

# Cek Gambar Overlay Punya Channel Alpha ('A')
if 'A' in overlay_image.getbands():
     # Jika Ada, Ambil Alpha Channel & Konversi Overlay Ke RGB
    alpha = overlay_image.split()[3] # Dipisah Menjadi 3 Saluran
    overlay_image = overlay_image.convert('RGB')
    overlay_image.putalpha(alpha) # Mengembalikan Nilai Alpha Yang Sebelumnya Diconvert Menjadi RGB

# Menentukan Ukuran Maksimum Overlay
max_size = (300, 300)
overlay_image.thumbnail(max_size)

# Menghitung Posisi Tengah (Horizontal) Untuk Overlay
x_center = (background_image.width - overlay_image.width) // 2
# Menentukan Posisi (Vertikal) Untuk Overlay
y_center = 10

# Menempelkan Overlay Di Atas Background Pada Posisi Yang Telah Ditentukan
background_image.paste(overlay_image, (x_center, y_center), overlay_image)

# # Menyimpan Gambar Dengan Nama File Yang Ditentukan
background_image.save("hasil_edit.jpg")

background_image.show()