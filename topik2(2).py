def convert_to_int(string):
    try:
        result = int(string)
        return result
    except ValueError:
        return "Error: Input harus berupa angka."

# Contoh penggunaan
umur = input('Masukkan umur kamu: ')  # Input yang benar adalah angka

umur5tahunlagi = convert_to_int(umur)

if isinstance(umur5tahunlagi, int):
    print(f"Umur kamu 5 tahun lagi adalah {umur5tahunlagi + 5}")
else:
    print(umur5tahunlagi)  # Menampilkan pesan error jika input bukan angka