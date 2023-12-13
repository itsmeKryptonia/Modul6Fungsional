from PIL import Image, ImageEnhance # Python Imaging Library

# Buka gambar dengan Pillow
image = Image.open("C:/Users/User/OneDrive/Dokumen/SYSTEM 56/KELAS A/TUGAS KULIAH SEMESTER 5/Pemograman Fungsional/Praktikum/Latihan/Modul 6/Kegiatan3/Background/UMM.jpg")  

# Ubah Tingkat Kecerahan & Kontras
brightness_factor = 1.5 # Kecerahan
contrast_factor = 1.2 # Kontras

# Enhancer Untuk Kecerahan 
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(brightness_factor)

# Enhancer Untuk Kontras
enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(contrast_factor)

# Menyimpan Gambar Dengan Nama File Yang Ditentukan
final_image.save("brightness_contrast_image.jpg")

final_image.show()