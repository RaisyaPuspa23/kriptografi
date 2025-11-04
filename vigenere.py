import string
from collections import Counter

# Huruf A sampai Z
ALPH = string.ascii_uppercase

# Bersihin teks biar cuma huruf aja dan huruf besar semua
def normalize(s):
    return "".join(ch for ch in s.upper() if ch.isalpha())

# Fungsi buat enkripsi (mengubah teks asli jadi ciphertext)
def vigenere_encrypt(plaintext, key):
    pt = normalize(plaintext)
    key = normalize(key)
    ct_chars = []
    klen = len(key)
    for i, ch in enumerate(pt):
        shift = ord(key[i % klen]) - 65
        ct_chars.append(chr((ord(ch) - 65 + shift) % 26 + 65))
    return "".join(ct_chars)

# Fungsi buat dekripsi (mengubah ciphertext jadi teks asli)
def vigenere_decrypt(ciphertext, key):
    ct = normalize(ciphertext)
    key = normalize(key)
    pt_chars = []
    klen = len(key)
    for i, ch in enumerate(ct):
        shift = ord(key[i % klen]) - 65
        pt_chars.append(chr((ord(ch) - 65 - shift) % 26 + 65))
    return "".join(pt_chars)

# Fungsi buat hitung frekuensi huruf
def frequency_analysis(text):
    t = normalize(text)
    total = len(t)
    cnt = Counter(t)
    table = [(ch, cnt.get(ch,0), (cnt.get(ch,0)/total*100 if total>0 else 0)) for ch in ALPH]
    return table

# Contoh penggunaan (kamu bisa ubah plaintext & key-nya)
if __name__ == "__main__":
    plaintext = "VIGENERE CIPHER IS MORE SECURE THAN CAESAR"
    key = "KEY"

    ciphertext = vigenere_encrypt(plaintext, key)
    decrypted = vigenere_decrypt(ciphertext, key)
    freq_table = frequency_analysis(ciphertext)

    print("Plaintext :", plaintext)
    print("Key        :", key)
    print("Ciphertext :", ciphertext)
    print("Decrypted  :", decrypted)
    print("\n--- Frequency Table ---")
    print("Huruf | Jumlah | Persentase")
    for ch,count,perc in freq_table:
        if count>0:
            print(f"{ch:>3}   |   {count:>2}    |   {perc:5.2f}%")
