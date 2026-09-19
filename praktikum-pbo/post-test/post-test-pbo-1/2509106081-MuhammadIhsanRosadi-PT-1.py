class Klien:
    def __init__(self, nama, instansi, anggaran):
        self.nama = nama
        self.instansi = instansi
        self.__anggaran = anggaran

    @property
    def anggaran(self):
        return self.__anggaran

    @anggaran.setter
    def anggaran(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)):
            raise ValueError("Anggaran harus berupa angka!")
        if nilai_baru < 0:
            raise ValueError("Anggaran tidak boleh negatif!")
        self.__anggaran = nilai_baru

    def tampilkan_info(self):
        print(f"Klien: {self.nama} ({self.instansi}) - Anggaran: Rp{self.anggaran:,.2f}")


class Layanan:
    def __init__(self, nama_jasa, harga, estimasi_hari):
        self.nama_jasa = nama_jasa
        self.harga = harga
        self.estimasi_hari = estimasi_hari

    def info_layanan(self):
        print(f"Jasa: {self.nama_jasa} | Harga: Rp{self.harga:,.2f} | Estimasi: {self.estimasi_hari} hari")

    @classmethod
    def dari_string(cls, data_string):
        nama, harga, hari = data_string.split('-')
        return cls(nama, float(harga), int(hari))


class Pesanan:
    nama_studio = "MondayCraft Studio"
    total_pesanan = 0
    pajak_persen = 11

    def __init__(self, klien, layanan):
        self.klien = klien
        self.layanan = layanan
        Pesanan.total_pesanan += 1
        self.id_pesanan = f"ORD-{Pesanan.total_pesanan:03d}"

    def cetak_invoice(self):
        total_biaya = self.hitung_total(self.layanan.harga, Pesanan.pajak_persen)
        print(f"--- INVOICE {self.id_pesanan} ---")
        print(f"Studio    : {Pesanan.nama_studio}")
        print(f"Pemesan   : {self.klien.nama}")
        print(f"Jasa UI/UX: {self.layanan.nama_jasa}")
        print(f"Total Tagihan (termasuk pajak {Pesanan.pajak_persen}%): Rp{total_biaya:,.2f}")

    @classmethod
    def ubah_pajak_studio(cls, pajak_baru):
        cls.pajak_persen = pajak_baru
        print(f"Pajak {cls.nama_studio} diubah menjadi {cls.pajak_persen}%")

    @staticmethod
    def hitung_total(harga_dasar, pajak):
        return harga_dasar + (harga_dasar * pajak / 100)

if __name__ == "__main__":
    klien1 = Klien("Budi", "PT Maju Terus", 15000000)
    klien2 = Klien("Siti", "Startup Kreatif", 5000000)

    layanan1 = Layanan("Redesign Landing Page", 3500000, 7)
    layanan2 = Layanan.dari_string("Mobile App Prototype-8000000-14")

    pesanan1 = Pesanan(klien1, layanan1)
    pesanan2 = Pesanan(klien2, layanan2)

    print("\n~ Informasi Klien dan Layanan")
    klien1.tampilkan_info()
    layanan1.info_layanan()
    klien2.tampilkan_info()
    layanan2.info_layanan()
    
    print("\n~ Memanggil Static Method secara langsung")
    estimasi = Pesanan.hitung_total(1000000, 11)
    print(f"Harga 1jt + Pajak 11%: Rp{estimasi:,.2f}")

    print("\n~ Mencetak invoice pesanan 1")
    pesanan1.cetak_invoice()

    print("\n~ Mengubah pajak untuk seluruh pesanan studio menggunakan Class Method")
    Pesanan.ubah_pajak_studio(12) 

    print("\n~ Mencetak invoice pesanan 2 dengan pajak baru")
    pesanan2.cetak_invoice()

    print("\n~ Menguji setter dengan data yang valid")
    klien1.anggaran = 20000000 
    print(f"Anggaran klien1 sekarang: Rp{klien1.anggaran:,.2f}")

    print("\n~ Menguji setter dengan data yang tidak valid")
    try:
        klien1.anggaran = -20000000 
    except ValueError as e:
        print(f"error validasi: {e}")
    print(f"Anggaran klien1 sekarang: Rp{klien1.anggaran:,.2f}")

    print("\n~ Menguji setter dengan tipe data yang salah")
    try: 
        klien1.anggaran = "Kosong"
    except ValueError as e:
        print(f"error validasi: {e}")
    print(f"Anggaran klien1 sekarang: Rp{klien1.anggaran:,.2f}")