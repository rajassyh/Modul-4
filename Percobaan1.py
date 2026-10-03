# ================================================
# Tugas Praktikum Modul 4 - Function & Method
# Program Simulasi Antrean Praktikum Lab Komputer
# Watermark: Kelompok 37
# ================================================
 
# ---------- FUNCTION (Return Type) ----------
 
def hitung_estimasi_waktu(jumlah_peserta,
                           waktu_per_orang):
    total_waktu = jumlah_peserta * waktu_per_orang
    return total_waktu
 
def status_lab():
    jam_sekarang = 14
    if jam_sekarang >= 8 and jam_sekarang <= 16:
        return "Lab sedang BUKA"
    else:
        return "Lab sedang TUTUP"
 
# ---------- CLASS & METHOD (Non-Return Type) ----------
 
class Praktikum:
    def __init__(self, nama_modul, kelompok):
        self.nama_modul = nama_modul
        self.kelompok = kelompok
        self.daftar_sesi = [
            "Sesi 1 - Pengenalan Alat",
            "Sesi 2 - Praktik Mandiri",
            "Sesi 3 - Asistensi"
        ]
 
    def tampilkan_jadwal(self):
        print(f"Jadwal praktikum {self.nama_modul} "
              f"untuk {self.kelompok}:")
        for sesi in self.daftar_sesi:
            print(f"- {sesi}")
 
    def catat_kehadiran(self, nama, hadir):
        if hadir:
            pesan = (f"{nama} tercatat HADIR pada "
                     f"praktikum hari ini.")
            print(pesan)
        else:
            pesan = (f"{nama} tercatat TIDAK HADIR, "
                     f"wajib inhal.")
            print(pesan)
 
# ---------- PROGRAM UTAMA ----------
 
print("=== SIMULASI ANTREAN PRAKTIKUM LAB KOMPUTER ===")
print("Watermark: Kelompok 37")
print()
 
lab = Praktikum("Function & Method", "Kelompok 37")
lab.tampilkan_jadwal()
print("-" * 40)
 
print(status_lab())
print("-" * 40)
 
peserta = 5
waktu_tiap_orang = 4
estimasi = hitung_estimasi_waktu(
    peserta, waktu_tiap_orang)
print(f"Estimasi total waktu praktikum untuk {peserta} "
      f"peserta: {estimasi} menit")
print("-" * 40)
 
lab.catat_kehadiran("Dafa", True)
lab.catat_kehadiran("Rangga", False)
print("-" * 40)
 
antrean = 3
print("Hitung mundur giliran masuk lab:")
while antrean > 0:
    print(f"Nomor antrean {antrean} "
          f"dipersilakan masuk...")
    antrean -= 1
print("Antrean selesai, seluruh peserta sudah "
      "masuk lab.")
