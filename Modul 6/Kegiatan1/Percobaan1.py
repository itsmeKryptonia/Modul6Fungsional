from PIL import Image, ImageDraw, ImageFont # Python Imaging Library

# Membuka File Gambar Dengan PIL
gambarku = Image.open("C:/Users/User/OneDrive/Dokumen/SYSTEM 56/KELAS A/TUGAS KULIAH SEMESTER 5/Pemograman Fungsional/Praktikum/Latihan/Modul 6/Kegiatan1/Background/UMM.jpg")

# Mengubah Gambar Menjadi Hitam Putih
gambarBW = gambarku.convert("L")

# Membuat Objek Penggambaran Untuk Menggambar Di Gambar Hitam Putihnya
draw = ImageDraw.Draw(gambarBW)
# Path File Font
font_path = r"C:/Users/User/OneDrive/Dokumen/SYSTEM 56/KELAS A/TUGAS KULIAH SEMESTER 5/Pemograman Fungsional/Praktikum/Latihan/Modul 6/Kegiatan1/Arial.ttf"
font_size = 24

# Untuk Mencoba Memuat Font 
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print(f"Error loading font from {font_path}")
    font = ImageFont.load_default()

# Teks Pada Gambar Hitam Putih
text = "Nama: M Daffa Raihan S\nNIM: 202110370311022"

# Kotak Pembatas Ukuran Teks
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

# Rumus Posisi Tengah Untuk Teks
center_x = (gambarku.width - text_width) // 2
center_y = (gambarku.height - text_height) // 2

# Menggambar Teks Di Gambar Hitam Putih & Posisi Tengah
draw.text((center_x, center_y), text, font=font)

# Menyimpan Gambar Dengan Nama File Yang Ditentukan
gambarBW.save("percobaan_satu.jpg")
gambarBW.show()
