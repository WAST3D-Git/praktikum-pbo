from abc import ABC, abstractmethod

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
        self.__anggaran = 0
        self.anggaran = anggaran

    @property
    def anggaran(self):
        return self.__anggaran

    @anggaran.setter
    def anggaran(self, nilai_baru):
        if isinstance(nilai_baru, bool) or not isinstance(nilai_baru, (int, float)):
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

class Layanan(ABC):
    def __init__(self, nama_jasa, harga, estimasi_hari):
        if not isinstance(nama_jasa, str) or not nama_jasa.strip():
            raise ValueError("Nama jasa tidak boleh kosong!")
        if isinstance(harga, bool) or not isinstance(harga, (int, float)) or harga < 0:
            raise ValueError("Harga harus berupa angka dan tidak boleh negatif!")
        if isinstance(estimasi_hari, bool) or not isinstance(estimasi_hari, int) or estimasi_hari <= 0:
            raise ValueError("Estimasi hari harus berupa bilangan bulat positif!")
        self.nama_jasa = nama_jasa
        self.harga = harga
        self.estimasi_hari = estimasi_hari

    @abstractmethod
    def jenis_layanan(self):
        pass

    @abstractmethod
    def rincian_tambahan(self):
        pass

    def info_layanan(self):
        print(
            f"Jasa: {self.nama_jasa} | Jenis: {self.jenis_layanan()} | "
            f"Harga: Rp{self.harga:,.2f} | Estimasi: {self.estimasi_hari} hari | "
            f"{self.rincian_tambahan()}"
        )

    @classmethod
    def dari_string(cls, data_string, **detail):
        try:
            nama, harga_teks, hari_teks = data_string.rsplit("-", 2)
            harga = float(harga_teks)
            hari = int(hari_teks)
        except (ValueError, TypeError) as e:
            raise ValueError("Format harus 'nama-harga-hari' dengan harga dan hari yang valid!") from e
        return cls(nama, harga, hari, **detail)

    def __str__(self):
        return f"{self.nama_jasa} ({self.jenis_layanan()}) - Rp{self.harga:,.2f}"

    def __lt__(self, layanan_lain):
        try:
            harga_lain = layanan_lain.harga
        except AttributeError:
            return NotImplemented
        return self.harga < harga_lain


class LayananDesainUI(Layanan):
    def __init__(self, nama_jasa, harga, estimasi_hari, platform_target="Web responsif"):
        super().__init__(nama_jasa, harga, estimasi_hari)
        self.platform_target = platform_target

    def jenis_layanan(self):
        return "Desain UI"

    def rincian_tambahan(self):
        return f"Platform target: {self.platform_target}"


class LayananRisetUX(Layanan):
    def __init__(self, nama_jasa, harga, estimasi_hari, metode_riset="Wawancara pengguna"):
        super().__init__(nama_jasa, harga, estimasi_hari)
        self.metode_riset = metode_riset

    def jenis_layanan(self):
        return "Riset UX"

    def rincian_tambahan(self):
        return f"Metode riset: {self.metode_riset}"


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
        self.pajak_persen = Pesanan.pajak_persen 
        total = self.hitung_total(layanan.harga, self.pajak_persen)
        self.pembayaran = Pembayaran(self.id_pesanan, total)

    def tambah_desainer(self, desainer):
        if desainer not in self.tim_desainer:
            self.tim_desainer.append(desainer)

    def keluarkan_desainer(self, nama):
        self.tim_desainer = [desainer for desainer in self.tim_desainer if desainer.nama != nama]

    def cetak_invoice(self):
        print(f"--- INVOICE {self.id_pesanan} ---")
        print(f"Studio    : {self.nama_studio}")
        print(f"Pemesan   : {self.klien.nama}")
        print(f"Jasa UI/UX: {self.layanan.nama_jasa}")
        print(f"Desainer  : {', '.join(desainer.nama for desainer in self.tim_desainer) or '-'}")
        print(
            f"Total Tagihan (termasuk pajak {self.pajak_persen}%): "
            f"Rp{self.pembayaran.total:,.2f}"
        )

    def __len__(self):
        return len(self.tim_desainer)

    @classmethod
    def ubah_pajak_studio(cls, pajak_baru):
        if isinstance(pajak_baru, bool) or not isinstance(pajak_baru, (int, float)) or pajak_baru < 0:
            raise ValueError("Pajak harus berupa angka dan tidak boleh negatif!")
        cls.pajak_persen = pajak_baru
        print(f"Pajak {cls.nama_studio} diubah menjadi {cls.pajak_persen}%")

    @staticmethod
    def hitung_total(harga_dasar, pajak):
        return harga_dasar + (harga_dasar * pajak / 100)

class NotifikasiEmail:
    def kirim(self, pesan):
        print(f"[Simulasi Email] {pesan}")

class NotifikasiKonsol:
    def kirim(self, pesan):
        print(f"[Notifikasi Konsol] {pesan}")

def kirim_notifikasi(kanal, pesan):    
    kanal.kirim(pesan)


if __name__ == "__main__":
    print("=" * 65)
    print("Sistem Manajemen Pemesanan Jasa Desain UI/UX pada Studio Digital")
    print("=" * 65)

    klien1 = Klien("Budi", "budi@maju.com", "pw123", "PT Maju Terus", 15000000)
    desainer1 = Desainer("Sari", "sari@mc.id", "pw456", "UI Design")
    desainer2 = Desainer("Dimas", "dimas@mc.id", "pw789", "UX Research")
    layanan1 = LayananDesainUI.dari_string(
        "Redesign Landing Page-3500000-7", platform_target="Web responsif"
    )
    layanan2 = LayananRisetUX(
        "Riset Pengalaman Pengguna", 2500000, 5, "Wawancara + usability testing"
    )

    print("\n~ Menguji Inheritance: method overriding tampilkan_info()")
    pengguna_umum = Pengguna("Umum", "umum@mc.id", "pw000")
    daftar_pengguna = [pengguna_umum, klien1, desainer1]
    for pengguna in daftar_pengguna:
        pengguna.tampilkan_info()

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

    print("\n~ Menguji Abstraksi: abstract class dan method konkret")
    try:
        Layanan("Layanan Umum", 100000, 1)
    except TypeError as e:
        print(f"Layanan tidak dapat diinstansiasi: {e}")
    layanan1.info_layanan()
    layanan2.info_layanan()
    print(f"Objek layanan dari __str__: {layanan1}")

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
    print(f"Tim desainer: {[desainer.nama for desainer in pesanan1.tim_desainer]}")
    print(f"Jumlah desainer (len(pesanan1)): {len(pesanan1)}")
    pesanan1.cetak_invoice()

    print("\n~ Mengeluarkan Dimas dari pesanan (objek Dimas tidak dihapus)")
    pesanan1.keluarkan_desainer("Dimas")
    print(f"Tim desainer: {[desainer.nama for desainer in pesanan1.tim_desainer]}")
    print(f"Desainer2 masih ada: {desainer2.nama}")

    print("\n~ Menguji Komposisi: Pembayaran dibuat otomatis di dalam Pesanan")
    print(f"ID Pembayaran : {pesanan1.pembayaran.id_pesanan}")
    print(f"Status        : {pesanan1.pembayaran.status}")
    pesanan1.pembayaran.bayar()

    print("\n~ Menghapus Pesanan (bukti siklus hidup agregasi vs komposisi)")
    import gc
    import weakref

    ref_pembayaran = weakref.ref(pesanan1.pembayaran)
    del pesanan1
    gc.collect()
    print(f"Klien masih ada      : {klien1.nama}")
    print(f"Layanan masih ada    : {layanan1.nama_jasa}")
    print(f"Desainer1 masih ada  : {desainer1.nama}")
    print(f"Pembayaran masih ada? {ref_pembayaran() is not None}")

    print("\n~ Menguji Duck Typing: dua kelas memakai method kirim()")
    kirim_notifikasi(NotifikasiEmail(), "Pesanan Redesign Landing Page telah diperbarui.")
    kirim_notifikasi(NotifikasiKonsol(), "Pesanan Redesign Landing Page telah diperbarui.")

    print("\n~ Menguji Operator Overloading: operator < dan fungsi len()")
    print(f"Riset UX lebih murah daripada Desain UI? {layanan2 < layanan1}")
    print(f"Representasi teks layanan: {str(layanan1)}")