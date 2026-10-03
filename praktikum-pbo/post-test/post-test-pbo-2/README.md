# Sistem Manajemen Pesanan UI/UX pada Studio Digital

## 1. Penjelasan Program

Program ini adalah simulasi sistem manajemen pesanan sederhana berbasis **Object-Oriented Programming (OOP)** menggunakan Python. Program ini dirancang untuk mencatat data pengguna (klien dan desainer), mendaftar layanan yang ditawarkan oleh studio, memproses pesanan hingga mencetak invoice tagihan, serta mencatat pembayaran.

Program ini mengimplementasikan beberapa pilar dan fitur OOP pada Python, antara lain:

- **Enkapsulasi (Encapsulation)**: mengamankan data sensitif menggunakan atribut private dan mengelolanya dengan getter/setter.
- **Inheritance (Pewarisan)**: `Klien` dan `Desainer` mewarisi class `Pengguna`, lengkap dengan `super().__init__()`, atribut unik, method overriding, serta atribut protected dan private.
- **Relasi UML**: menerapkan **Asosiasi**, **Agregasi**, dan **Komposisi** antar class.
- **Class Method & Static Method**: `@classmethod` untuk alternative constructor dan mengubah state global class, serta `@staticmethod` untuk fungsi utilitas yang tidak terikat pada instance.

---

## 2. Struktur Class

Program ini terdiri dari enam class.

```
Pengguna (superclass)
 ├─ Klien      (subclass)
 └─ Desainer   (subclass)

Layanan
Pesanan
Pembayaran
```

### A. Class `Pengguna` (Superclass)

Merepresentasikan pengguna sistem secara umum. Menjadi parent class bagi `Klien` dan `Desainer`.

**Atribut**

| Atribut | Akses | Keterangan |
|---|---|---|
| `nama` | Public | Nama pengguna |
| `_email` | Protected | Email pengguna, dapat diakses langsung oleh subclass |
| `__password` | Private | Kata sandi, hanya dapat diakses dari dalam `Pengguna` |

**Method Utama**

- `__init__`: konstruktor inisialisasi atribut pengguna.
- `cek_password(input_pw)`: memverifikasi password tanpa membuka atribut private.
- `tampilkan_info()`: mencetak informasi dasar pengguna (akan di-override oleh subclass).

### B. Class `Klien` (Subclass dari `Pengguna`)

Merepresentasikan pelanggan yang menggunakan jasa studio.

**Atribut Tambahan (unik)**

| Atribut | Akses | Keterangan |
|---|---|---|
| `instansi` | Public | Nama perusahaan atau instansi klien |
| `__anggaran` | Private | Dana yang dimiliki klien |

**Method Utama**

- `__init__`: memanggil `super().__init__(nama, email, password)` lalu mengisi `instansi` dan `__anggaran`.
- `@property anggaran`: getter untuk mengakses nilai anggaran yang di-private.
- `@anggaran.setter`: setter untuk mengubah nilai anggaran dengan validasi.
- `tampilkan_info()`: **override** dari `Pengguna`, menampilkan nama, instansi, dan anggaran.

### C. Class `Desainer` (Subclass dari `Pengguna`)

Merepresentasikan desainer UI/UX yang mengerjakan pesanan.

**Atribut Tambahan (unik)**

| Atribut | Akses | Keterangan |
|---|---|---|
| `spesialisasi` | Public | Bidang keahlian desainer |

**Method Utama**

- `__init__`: memanggil `super().__init__(nama, email, password)` lalu mengisi `spesialisasi`.
- `tampilkan_info()`: **override** dari `Pengguna`, menampilkan nama, email (`_email` protected), dan spesialisasi.
- `kerjakan(layanan)`: menerima objek `Layanan` sebagai parameter dan memakainya sementara (**asosiasi**).

### D. Class `Layanan`

Merepresentasikan produk jasa yang ditawarkan oleh studio.

**Atribut**

| Atribut | Tipe | Keterangan |
|---|---|---|
| `nama_jasa` | String | Nama layanan |
| `harga` | Float | Harga jasa tersebut |
| `estimasi_hari` | Int | Waktu pengerjaan dalam hari |

**Method Utama**

- `__init__`: konstruktor inisialisasi layanan.
- `info_layanan()`: mencetak informasi detail layanan.
- `@classmethod dari_string(cls, data_string)`: alternative constructor untuk membuat objek `Layanan` dari format string teks yang dipisahkan tanda strip.

### E. Class `Pembayaran`

Merepresentasikan pembayaran dari sebuah pesanan. Objek ini dibuat dan dimiliki oleh `Pesanan`.

**Atribut**

| Atribut | Tipe | Keterangan |
|---|---|---|
| `id_pesanan` | String | ID pesanan yang dibayar |
| `total` | Float | Total tagihan (sudah termasuk pajak) |
| `status` | String | `"Belum Lunas"` atau `"Lunas"` |

**Method Utama**

- `bayar()`: mengubah status menjadi `"Lunas"` dan mencetak konfirmasi.

### F. Class `Pesanan`

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
| `klien` | Object | Objek `Klien` yang dikirim dari luar (agregasi) |
| `layanan` | Object | Objek `Layanan` yang dikirim dari luar (agregasi) |
| `tim_desainer` | List | Daftar objek `Desainer` yang dikirim dari luar (agregasi) |
| `id_pesanan` | String | ID pesanan unik hasil auto-generate |
| `pembayaran` | Object | Objek `Pembayaran` yang dibuat di dalam `Pesanan` (komposisi) |

**Method Utama**

- `__init__`: konstruktor inisialisasi pesanan, menerima klien & layanan, membuat ID, dan membuat objek `Pembayaran`.
- `tambah_desainer(desainer)`: menambahkan desainer ke dalam pesanan.
- `keluarkan_desainer(nama)`: melepas desainer dari pesanan tanpa menghapus objek `Desainer`.
- `cetak_invoice()`: mencetak struk tagihan termasuk daftar desainer dan total biaya yang sudah ditambah pajak.
- `@classmethod ubah_pajak_studio(cls, pajak_baru)`: mengubah persentase pajak untuk seluruh transaksi di dalam studio.
- `@staticmethod hitung_total(harga_dasar, pajak)`: fungsi utilitas matematika independen untuk menghitung total harga akhir + pajak.

---

## 3. Penerapan Relasi UML

| Relasi | Kata Kunci | Penerapan di Program |
|---|---|---|
| **Asosiasi** | "menggunakan" | `Desainer.kerjakan(layanan)` menerima `Layanan` lewat parameter method dan **tidak menyimpannya** sebagai atribut. |
| **Agregasi** | "memiliki" | `Pesanan` menampung `Klien`, `Layanan`, dan daftar `Desainer` yang dibuat di luar lalu dikirim lewat konstruktor/method. Jika `Pesanan` dihapus, objek-objek tersebut **tetap ada**. |
| **Komposisi** | "terdiri dari" | `Pesanan` membuat `Pembayaran` langsung di dalam konstruktornya. Jika `Pesanan` dihapus, `Pembayaran` **ikut musnah**. |

```
Desainer ┈┈┈ menggunakan ┈┈┈> Layanan          (Asosiasi)
Pesanan  ◇─── memiliki ───── Klien, Layanan, Desainer   (Agregasi)
Pesanan  ◆─── terdiri dari ─ Pembayaran        (Komposisi)
Klien, Desainer ───▷ Pengguna                  (Pewarisan)
```

---

## 4. Penerapan Inheritance

| Persyaratan | Penerapan di Program |
|---|---|
| Superclass & subclass | Superclass `Pengguna`; subclass `Klien` dan `Desainer`. |
| Penggunaan `super()` | Kedua subclass memanggil `super().__init__(nama, email, password)`. |
| Atribut tambahan | `Klien`: `instansi` dan `__anggaran`. `Desainer`: `spesialisasi`. |
| Method overriding | `tampilkan_info()` di-override oleh `Klien` dan `Desainer`. |
| Protected (`_nama`) | `_email` pada `Pengguna`, dipakai langsung oleh `Desainer.tampilkan_info()`. |
| Private (`__nama`) | `__password` pada `Pengguna`, hanya bisa diverifikasi lewat `cek_password()`. |

---

## 5. Panduan Pengujian

Blok `if __name__ == "__main__":` di dalam kode sudah dilengkapi dengan skenario pengujian. Berikut adalah panduan cara menjalankan dan mengevaluasi hasilnya.

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

1. **Inheritance: Method Overriding**
   - Program memanggil `tampilkan_info()` pada objek `Pengguna`, `Klien`, dan `Desainer`.
   - **Ekspektasi:** Ketiganya menampilkan format yang berbeda (hasil override).

2. **Inheritance: `super().__init__()`**
   - Program menampilkan `nama` dan `_email` milik objek `Klien` dan `Desainer`.
   - **Ekspektasi:** Atribut dari superclass terisi pada kedua subclass.

3. **Atribut Tambahan Tiap Subclass**
   - **Ekspektasi:** `Klien` punya `instansi` tetapi tidak punya `spesialisasi`; `Desainer` punya `spesialisasi` tetapi tidak punya `instansi` (`False` pada pengecekan `hasattr`).

4. **Atribut Protected (`_email`)**
   - **Ekspektasi:** Email desainer berhasil dibaca langsung lewat subclass.

5. **Atribut Private (`__password`)**
   - Program mencoba mengakses `klien1.__password` secara langsung.
   - **Ekspektasi:** Muncul `AttributeError`. Lewat `cek_password()`, password benar menghasilkan `True` dan password salah menghasilkan `False`.

6. **Asosiasi**
   - Program memanggil `desainer1.kerjakan(layanan1)` dan `desainer2.kerjakan(layanan1)`.
   - **Ekspektasi:** Muncul pesan pengerjaan layanan, dan `hasattr(desainer1, 'layanan')` bernilai `False` karena layanan tidak disimpan.

7. **Agregasi**
   - Program membuat `pesanan1`, menambahkan `desainer1` dan `desainer2`, lalu mencetak invoice.
   - **Ekspektasi:** Invoice menampilkan ID `"ORD-001"`, daftar desainer, dan total `Rp3.885.000,00` (pajak 11%).
   - Program lalu mengeluarkan `Dimas` dari pesanan.
   - **Ekspektasi:** Tim desainer tinggal `['Sari']`, namun objek `desainer2` tetap ada.

8. **Komposisi**
   - Program menampilkan `id_pesanan` dan status `Pembayaran` milik `pesanan1`, lalu memanggil `bayar()`.
   - **Ekspektasi:** ID Pembayaran `"ORD-001"`, status awal `"Belum Lunas"`, lalu berubah menjadi `"Lunas"`.

9. **Siklus Hidup Saat Pesanan Dihapus**
   - Program menjalankan `del pesanan1`.
   - **Ekspektasi:** `Klien`, `Layanan`, dan `Desainer` (agregasi/asosiasi) **masih ada**, sedangkan `Pembayaran` (komposisi) **sudah musnah** (`False`).

> **Catatan:** Fitur `@classmethod`, `@staticmethod`, dan setter `anggaran` (dengan validasi) tetap ada di dalam kode, tetapi tidak dijalankan pada blok pengujian ini karena pengujian difokuskan pada relasi UML dan inheritance.