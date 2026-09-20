# Sistem Manajemen Pesanan UI/UX pada Studio Digital

## 1. Penjelasan Program

Program ini adalah simulasi sistem manajemen pesanan sederhana berbasis **Object-Oriented Programming (OOP)** menggunakan Python. Program ini dirancang untuk mencatat data klien, mendaftar layanan yang ditawarkan oleh studio, serta memproses pesanan hingga mencetak invoice tagihan.

Program ini mengimplementasikan beberapa pilar dan fitur tingkat lanjut OOP pada Python, antara lain:

- **Enkapsulasi (Encapsulation)** — Mengamankan data sensitif menggunakan private attribute dan mengelolanya dengan getter/setter.
- **Komposisi (Composition)** — Objek `Pesanan` dibangun dari gabungan objek `Klien` dan `Layanan`.
- **Class Method & Static Method** — Menggunakan `@classmethod` untuk alternative constructor dan mengubah state global class, serta `@staticmethod` untuk fungsi utilitas yang tidak terikat pada instance.

---

## 2. Struktur Class

Program ini terdiri dari tiga class utama.

### A. Class `Klien`

Merepresentasikan pelanggan yang menggunakan jasa studio.

**Atribut**

| Atribut | Tipe | Keterangan |
|---|---|---|
| `nama` | String | Nama klien |
| `instansi` | String | Nama perusahaan atau instansi klien |
| `__anggaran` | Private | Dana yang dimiliki klien |

**Method Utama**

- `__init__` — Konstruktor untuk inisialisasi atribut klien.
- `@property anggaran` — Getter untuk mengakses nilai anggaran yang di-private.
- `@anggaran.setter` — Setter untuk mengubah nilai anggaran dengan validasi.
- `tampilkan_info()` — Mencetak informasi detail mengenai klien.

### B. Class `Layanan`

Merepresentasikan produk jasa yang ditawarkan oleh studio.

**Atribut**

| Atribut | Tipe | Keterangan |
|---|---|---|
| `nama_jasa` | String | Nama layanan |
| `harga` | Float | Harga jasa tersebut |
| `estimasi_hari` | Int | Waktu pengerjaan dalam hari |

**Method Utama**

- `__init__` — Konstruktor inisialisasi layanan.
- `info_layanan()` — Mencetak informasi detail layanan.
- `@classmethod dari_string(cls, data_string)` — Alternative constructor untuk membuat objek `Layanan` dari format string teks yang dipisahkan tanda strip.

### C. Class `Pesanan`

Merepresentasikan transaksi antara klien dan studio untuk layanan tertentu.

**Class Attribute**

| Atribut | Keterangan |
|---|---|
| `nama_studio` | `"MondayCraft Studio"` |
| `total_pesanan` | Pencatat jumlah pesanan yang dibuat (digunakan untuk auto-generate ID) |
| `pajak_persen` | Persentase pajak yang berlaku |

**Instance Attribute**

| Atribut | Tipe | Keterangan |
|---|---|---|
| `klien` | Object | Menyimpan objek dari class `Klien` |
| `layanan` | Object | Menyimpan objek dari class `Layanan` |
| `id_pesanan` | String | ID pesanan unik hasil auto-generate |

**Method Utama**

- `__init__` — Konstruktor inisialisasi pesanan, menyambungkan klien & layanan, serta membuat ID.
- `cetak_invoice()` — Mencetak struk tagihan termasuk total biaya yang sudah ditambah pajak.
- `@classmethod ubah_pajak_studio(cls, pajak_baru)` — Mengubah persentase pajak untuk seluruh transaksi di dalam studio.
- `@staticmethod hitung_total(harga_dasar, pajak)` — Fungsi utilitas matematika independen untuk menghitung total harga akhir + pajak.

---

## 3. Panduan Pengujian

Blok `if __name__ == "__main__":` di dalam kode sudah dilengkapi dengan skenario pengujian lengkap. Berikut adalah panduan cara menjalankan dan mengevaluasi hasilnya.

### Cara Menjalankan Program

1. Pastikan Anda memiliki Python 3.x terinstal di sistem Anda.
2. Simpan kode program ke dalam sebuah file, misalnya `main.py`.
3. Buka Terminal atau Command Prompt.
4. Navigasikan ke direktori tempat file disimpan, lalu jalankan perintah:
   ```bash
   python main.py
   ```

### Skenario Pengujian

Saat dijalankan, program akan melakukan pengujian secara berurutan:

1. **Instansiasi Objek**
   - Program membuat 2 objek untuk setiap class.

2. **Menampilkan Informasi Klien dan Layanan**
   - Output akan menampilkan list klien dan layanan beserta harganya.

3. **Menguji Static Method**
   - Program akan mencoba fungsi kalkulator pajak independen.
   - **Ekspektasi:** Muncul hasil kalkulasi `1.110.000`.

4. **Menguji Cetak Invoice**
   - Program mencetak `pesanan1`.
   - **Ekspektasi:** Muncul format invoice lengkap dengan ID `"ORD-001"` dan perhitungan pajak 11%.

5. **Uji Class Method**
   - Program mengubah pajak studio menjadi 12% melalui class method.
   - Kemudian mencetak `pesanan2` (ID: `"ORD-002"`).
   - **Ekspektasi:** Kalkulasi total pada invoice pesanan ke-2 akan menggunakan pajak 12%, bukan 11% lagi.

6. **Uji Validasi Setter (Enkapsulasi)**
   - **Kasus Valid:** Mengubah anggaran `klien1` menjadi `20.000.000`. Program akan menerimanya dan menampilkannya.
   - **Kasus Negatif:** Mengubah anggaran menjadi `-20000000`.
     - **Ekspektasi:** Program menangkap `ValueError` (`"Anggaran tidak boleh negatif!"`) dan membiarkan anggaran tetap di angka terakhir yang valid.
   - **Kasus Tipe Data Salah:** Mengubah anggaran menjadi string `"Kosong"`.
     - **Ekspektasi:** Program menangkap `ValueError` (`"Anggaran harus berupa angka!"`) dan melindungi aplikasi dari crash.
