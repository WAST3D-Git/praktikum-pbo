# Sistem Manajemen Pemesanan Jasa Desain UI/UX pada Studio Digital

## 1. Deskripsi Program

Program ini memodelkan proses pemesanan jasa desain UI/UX pada MondayCraft Studio. Fitur utamanya meliputi pengelolaan pengguna, klien, desainer, layanan desain UI dan riset UX, pesanan, invoice, pajak, serta status pembayaran.

Program juga menunjukkan penerapan konsep Pemrograman Berorientasi Objek (PBO), yaitu inheritance, enkapsulasi, abstraksi, polimorfisme, relasi antarkelas, dan prinsip SOLID. Ketika dijalankan, program menampilkan contoh penggunaan fitur-fitur tersebut di terminal.

### Cara Menjalankan

Pastikan Python 3.9 atau versi lebih baru telah terpasang. Program hanya menggunakan standard library Python sehingga tidak memerlukan instalasi paket tambahan.

```bash
python 2509106081-MuhammadIhsanRosadi-PT-3.py
```

## 2. Class Diagram UML

![Class Diagram UML Sistem Manajemen Pemesanan Jasa Desain UI/UX pada Studio Digital](UML.svg)

### Relasi Antarkelas

**Asosiasi: `Desainer` → `Layanan`.**
Desainer memakai layanan saat mengerjakannya, lewat method `Desainer.kerjakan(layanan)`. Relasinya asosiasi karena keduanya adalah objek yang berdiri sendiri dan hanya saling berhubungan saat method dipanggil, tanpa saling memiliki.

**Agregasi: `Pesanan` ◇→ `Klien`, `Layanan`, dan `Desainer`.**
Pesanan menampung klien, layanan, dan tim desainer yang dibuat di luar `Pesanan` lalu dimasukkan lewat konstruktor atau `tambah_desainer()`. Relasinya agregasi karena objek-objek itu tetap hidup walau pesanan dihapus, misalnya desainer yang sama bisa dipakai di pesanan lain.

**Komposisi: `Pesanan` ◆→ `Pembayaran`.**
Pesanan membuat objek `Pembayaran` sendiri di dalam konstruktornya, sehingga pembayaran adalah bagian dari pesanan itu. Relasinya komposisi karena pembayaran tidak punya arti tanpa pesanannya, jadi saat pesanan dihapus pembayarannya ikut hilang (terbukti di output dengan `weakref`).

## 3. Abstraksi (*Abstract Base Class*)

- **Abstract class:** `Layanan`, yang mewarisi `ABC` dari modul `abc`.
- **Abstract method:** `jenis_layanan()` dan `rincian_tambahan()`, keduanya menggunakan dekorator `@abstractmethod`.
- **Method konkret:** `info_layanan()` menampilkan informasi layanan umum dan menggunakan method yang diimplementasikan subclass. Kelas ini juga menyediakan `__str__()` dan `__lt__()`.
- **Subclass konkret:** `LayananDesainUI` mengimplementasikan kedua abstract method dan memiliki atribut khusus `platform_target`. `LayananRisetUX` juga mengimplementasikannya dan memiliki atribut khusus `metode_riset`.
- **Bukti abstract class tidak dapat diinstansiasi:** program mencoba membuat objek `Layanan(...)` dalam blok `try-except TypeError`. Pesan error ditampilkan di terminal karena kedua abstract method belum memiliki implementasi pada kelas dasar.

Abstraksi digunakan dalam alur program: pesanan menerima objek layanan dari kelas abstrak `Layanan`, sedangkan jenis layanan dan rincian khusus ditentukan oleh implementasi subclass masing-masing.

## 4. Polimorfisme

### a. Polimorfisme melalui Pewarisan

`Klien` dan `Desainer` adalah subclass `Pengguna` yang meng-*override* method `tampilkan_info()` dengan perilaku berbeda. Program menempatkan objek `Pengguna`, `Klien`, dan `Desainer` dalam satu daftar, lalu memanggil `tampilkan_info()` melalui satu perulangan. Setiap objek menjalankan implementasinya sendiri tanpa pemeriksaan tipe objek.

### b. Duck Typing

`NotifikasiEmail` dan `NotifikasiKonsol` tidak memiliki hubungan pewarisan satu sama lain, tetapi keduanya menyediakan method `kirim(pesan)`. Fungsi `kirim_notifikasi(kanal, pesan)` cukup memanggil `kanal.kirim(pesan)` tanpa memeriksa tipe objek. Pengiriman email pada contoh ini merupakan simulasi dan tidak mengirim email sungguhan.

### c. Operator Overloading

- `Layanan.__lt__()` memungkinkan operator `<` membandingkan harga dua layanan dan menghasilkan nilai boolean.
- `Layanan.__str__()` menyediakan representasi teks ketika objek ditampilkan dengan `str()` atau `print()`.
- `Pesanan.__len__()` membuat `len(pesanan)` mengembalikan jumlah desainer yang sedang ditugaskan.

Program tidak menggunakan rantai `if/elif` yang memeriksa `type()` atau nama kelas untuk menentukan perilaku polimorfik.

## 5. Bukti Output Eksekusi

Screenshot berikut menunjukkan output aktual program saat `python 2509106081-MuhammadIhsanRosadi-PT-3.py` dijalankan, termasuk overriding, error saat abstract class diinstansiasi, penggunaan asosiasi/agregasi/komposisi, invoice dan pembayaran, duck typing, serta operator overloading menggunakan ekstensi vscode bernama TermSnap.

![Screenshot output program](Screenshot-Output.png)

## 6. Prinsip SOLID

Program menerapkan **Open/Closed Principle (OCP)** pada hierarki `Layanan`. Jenis layanan baru dapat ditambahkan sebagai subclass yang mengimplementasikan abstract method tanpa perlu mengubah alur umum pemesanan dan pencetakan invoice. Dengan demikian, fitur layanan dapat diperluas tanpa menambahkan percabangan berdasarkan nama atau tipe layanan.
