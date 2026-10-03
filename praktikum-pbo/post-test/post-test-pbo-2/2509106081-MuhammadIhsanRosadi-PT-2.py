class Pengguna:                                   
    def __init__(self, nama, email, password):
        self.nama = nama
        self._email = email                       
        self.__password = password                

    def cek_password(self, input_pw):
        return self.__password == input_pw

    def tampilkan_info(self):
        print(f"Pengguna: {self.nama} ({self._email})")


class Klien(Pengguna):                            
    def __init__(self, nama, email, password, instansi, anggaran):
        super().__init__(nama, email, password)
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


class Desainer(Pengguna):                         
    def __init__(self, nama, email, password, spesialisasi):
        super().__init__(nama, email, password)
        self.spesialisasi = spesialisasi          

    def tampilkan_info(self):                     
        print(f"Desainer: {self.nama} ({self._email}) - Spesialisasi: {self.spesialisasi}")

    def kerjakan(self, layanan):
        print(f"{self.nama} mengerjakan layanan '{layanan.nama_jasa}' ({layanan.estimasi_hari} hari)")


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


class Pembayaran:
    def __init__(self, id_pesanan, total):
        self.id_pesanan = id_pesanan
        self.total = total
        self.status = "Belum Lunas"

    def bayar(self):
        self.status = "Lunas"
        print(f"Pembayaran {self.id_pesanan} sebesar Rp{self.total:,.2f}: {self.status}")


class Pesanan:
    nama_studio = "MondayCraft Studio"
    total_pesanan = 0
    pajak_persen = 11

    def __init__(self, klien, layanan):
        self.klien = klien                        
        self.layanan = layanan                    
        self.tim_desainer = []                    
        Pesanan.total_pesanan += 1
        self.id_pesanan = f"ORD-{Pesanan.total_pesanan:03d}"
        total = self.hitung_total(layanan.harga, Pesanan.pajak_persen)
        self.pembayaran = Pembayaran(self.id_pesanan, total)  

    def tambah_desainer(self, desainer):
        self.tim_desainer.append(desainer)

    def keluarkan_desainer(self, nama):
        self.tim_desainer = [d for d in self.tim_desainer if d.nama != nama]

    def cetak_invoice(self):
        total_biaya = self.hitung_total(self.layanan.harga, Pesanan.pajak_persen)
        print(f"--- INVOICE {self.id_pesanan} ---")
        print(f"Studio    : {Pesanan.nama_studio}")
        print(f"Pemesan   : {self.klien.nama}")
        print(f"Jasa UI/UX: {self.layanan.nama_jasa}")
        print(f"Desainer  : {', '.join(d.nama for d in self.tim_desainer) or '-'}")
        print(f"Total Tagihan (termasuk pajak {Pesanan.pajak_persen}%): Rp{total_biaya:,.2f}")

    @classmethod
    def ubah_pajak_studio(cls, pajak_baru):
        cls.pajak_persen = pajak_baru
        print(f"Pajak {cls.nama_studio} diubah menjadi {cls.pajak_persen}%")

    @staticmethod
    def hitung_total(harga_dasar, pajak):
        return harga_dasar + (harga_dasar * pajak / 100)


if __name__ == "__main__":
    klien1 = Klien("Budi", "budi@maju.com", "pw123", "PT Maju Terus", 15000000)
    desainer1 = Desainer("Sari", "sari@mc.id", "pw456", "UI Design")
    desainer2 = Desainer("Dimas", "dimas@mc.id", "pw789", "UX Research")
    layanan1 = Layanan("Redesign Landing Page", 3500000, 7)

    print("\n~ Menguji Inheritance: method overriding tampilkan_info()")
    Pengguna("Umum", "umum@mc.id", "pw000").tampilkan_info()
    klien1.tampilkan_info()
    desainer1.tampilkan_info()

    print("\n~ Menguji super().__init__(): atribut dari superclass pada subclass")
    print(f"Klien    : nama={klien1.nama}, email={klien1._email}")
    print(f"Desainer : nama={desainer1.nama}, email={desainer1._email}")

    print("\n~ Menguji atribut tambahan tiap subclass")
    print(f"Klien    punya instansi     : {klien1.instansi}")
    print(f"Desainer punya spesialisasi : {desainer1.spesialisasi}")
    print(f"Klien punya spesialisasi? {hasattr(klien1, 'spesialisasi')}")
    print(f"Desainer punya instansi? {hasattr(desainer1, 'instansi')}")

    print("\n~ Menguji atribut Protected (_email) diakses subclass")
    print(f"Email desainer1: {desainer1._email}")

    print("\n~ Menguji atribut Private (__password)")
    try:
        print(klien1.__password)
    except AttributeError as e:
        print(f"error akses: {e}")
    print(f"Password benar? {klien1.cek_password('pw123')}")
    print(f"Password salah? {klien1.cek_password('salah')}")

    print("\n~ Menguji Asosiasi: Layanan dipakai Desainer lewat parameter method")
    desainer1.kerjakan(layanan1)
    desainer2.kerjakan(layanan1)
    print(f"Desainer1 menyimpan layanan? {hasattr(desainer1, 'layanan')}")

    print("\n~ Menguji Agregasi: Pesanan menampung Klien, Layanan, dan Desainer dari luar")
    pesanan1 = Pesanan(klien1, layanan1)
    pesanan1.tambah_desainer(desainer1)
    pesanan1.tambah_desainer(desainer2)
    print(f"Pemesan     : {pesanan1.klien.nama}")
    print(f"Layanan     : {pesanan1.layanan.nama_jasa}")
    print(f"Tim desainer: {[d.nama for d in pesanan1.tim_desainer]}")
    pesanan1.cetak_invoice()

    print("\n~ Mengeluarkan Dimas dari pesanan (objek Dimas tidak dihapus)")
    pesanan1.keluarkan_desainer("Dimas")
    print(f"Tim desainer: {[d.nama for d in pesanan1.tim_desainer]}")
    print(f"Desainer2 masih ada: {desainer2.nama}")

    print("\n~ Menguji Komposisi: Pembayaran dibuat otomatis di dalam Pesanan")
    print(f"ID Pembayaran : {pesanan1.pembayaran.id_pesanan}")
    print(f"Status        : {pesanan1.pembayaran.status}")
    pesanan1.pembayaran.bayar()

    print("\n~ Menghapus Pesanan (bukti siklus hidup agregasi vs komposisi)")
    import weakref
    ref_pembayaran = weakref.ref(pesanan1.pembayaran)
    del pesanan1
    print(f"Klien masih ada      : {klien1.nama}")
    print(f"Layanan masih ada    : {layanan1.nama_jasa}")
    print(f"Desainer1 masih ada  : {desainer1.nama}")
    print(f"Pembayaran masih ada? {ref_pembayaran() is not None}")