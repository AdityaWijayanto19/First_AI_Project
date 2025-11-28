# Modul 0 – Setup Environment AI Development

Dokumen ini berisi panduan setup environment untuk pengembangan aplikasi AI menggunakan Python, Streamlit, dan Google AI (Gemini).

Setelah mengikuti langkah-langkah di bawah, kamu akan bisa:

- Mengikuti sesi belajar interaktif di **Google Colab**.
- Membangun dan menjalankan proyek aplikasi **Streamlit** secara lokal.
- Menggunakan **Python Virtual Environment (venv)** dengan praktik terbaik.

---

## 1. Objektif

Setelah menyelesaikan setup ini, kamu akan:

1. Siap menggunakan **Google Colab** untuk belajar (Modul 1 & 2).
2. Memiliki environment lokal untuk membangun dan menjalankan aplikasi **Streamlit** (Modul 3).
3. Memahami konsep dan penggunaan **Python Virtual Environment (venv)** sebagai ruang kerja yang rapi per proyek.

---

## 2. Prasyarat

Sebelum memulai, pastikan kamu memiliki:

- Komputer dengan **Windows**, **macOS**, atau **Linux**.
- Koneksi internet yang stabil.
- Akun Google (untuk **Google Colab** dan **Google AI Studio**).

---

## 3. Tools Utama yang Digunakan

### 3.1 Google Colab (Modul 1 & 2)

- **Apa itu?**  
  Layanan notebook berbasis cloud seperti Google Docs, tetapi untuk menulis dan menjalankan kode **Python**.
- **Kenapa dipakai?**  
  Tidak perlu install apa pun di komputer — semua berjalan di cloud (zero setup).
- **Akses:**  
  Buka: https://colab.research.google.com dan login dengan akun Google.

### 3.2 VS Code + Python Lokal (Modul 3)

- **Apa itu?**  
  Kombinasi **Python** di komputer lokal dan **Visual Studio Code (VS Code)** sebagai code editor.
- **Kenapa dipakai?**  
  Untuk membangun dan menjalankan aplikasi web **Streamlit** dari komputer kamu.
- **Akses:**  
  Python & VS Code akan diinstal pada langkah berikutnya.

### 3.3 Google AI API Key (Gemini)

- **Apa itu?**  
  API key pribadi untuk mengakses model AI **Gemini** dari Google.
- **Kenapa penting?**  
  Tanpa API key, aplikasi tidak bisa “berkomunikasi” dengan model AI.

---

## 4. Langkah 1 – Mendapatkan Google AI API Key

1. Buka **Google AI Studio** di browser:  
   https://aistudio.google.com (atau sesuai link resmi terbaru).
2. Login menggunakan akun Google-mu.
3. Klik tombol **"Get API Key"**.
4. Pilih **"Create API key in new project"**.
5. Copy API Key yang muncul (format biasanya diawali `AIza...`).
6. **Simpan API Key dengan aman**, misalnya di:
   - Password manager
   - File catatan lokal (bukan di repo publik)
7. **Jangan pernah** mempublikasikan API Key:
   - Jangan commit ke GitHub
   - Jangan tampilkan di screenshot atau dokumentasi publik

API key ini nanti akan dipakai di modul aplikasi (misalnya via file `.env` atau konfigurasi environment variable).

---

## 5. Langkah 2 – Setup Lingkungan Proyek Lokal

Langkah ini menyiapkan environment di komputer untuk menjalankan aplikasi **Streamlit** di Modul 3.

### 5.1 Instal Python

1. Buka: https://www.python.org/downloads/
2. Download versi Python terbaru (misalnya **Python 3.11** atau **3.12**).
3. **Khusus Windows:** saat instalasi, pastikan mencentang:
   > **"Add Python to PATH"** atau **"Add Python.exe to PATH"**
4. Lanjutkan proses instalasi sampai selesai.

### 5.2 Instal Visual Studio Code (VS Code)

1. Buka: https://code.visualstudio.com/
2. Download VS Code sesuai sistem operasi (Windows, macOS, atau Linux).
3. Install seperti biasa.

### 5.3 Instal Ekstensi Python di VS Code

1. Buka VS Code.
2. Klik tab **Extensions** (ikon kotak di sidebar kiri).
3. Cari: **“Python”** (publisher: Microsoft).
4. Klik **Install**.

### 5.4 Verifikasi Instalasi Python & pip

1. Buka **Terminal**:
   - Windows: `Command Prompt (CMD)` atau `PowerShell`
   - macOS/Linux: `Terminal`
2. Cek versi Python:

   ```bash
   python --version
   # jika error, coba:
   python3 --version
````

Harapan: muncul versi Python yang baru diinstall, contoh:

```text
Python 3.11.5
```

3. Cek versi pip:

   ```bash
   pip --version
   ```

   Harapan: muncul informasi versi pip, contoh:

   ```text
   pip 23.2.1 from ...
   ```

Jika kedua perintah berhasil, environment lokal sudah siap untuk pengembangan.

---

## 6. Langkah 3 – Konsep & Penggunaan Virtual Environment (venv)

Sebelum membuat proyek, kita akan menggunakan **Python Virtual Environment (venv)** agar setiap proyek punya “ruang kerja” sendiri.

> Analogi: Komputer = ruang tamu, venv = kamar kerja khusus tiap proyek.
> Library untuk proyek A tidak bercampur dengan proyek B.

### 6.1 Membuat Folder Proyek

Di terminal:

```bash
mkdir proyek-ai-pertama
cd proyek-ai-pertama
```

### 6.2 Membuat Virtual Environment

Masih di dalam folder proyek:

```bash
python -m venv venv
# jika gagal, coba:
python3 -m venv venv
```

Perintah ini akan membuat folder bernama `venv` di dalam proyek.

### 6.3 Mengaktifkan Virtual Environment

Perintah berbeda tergantung OS:

* **Windows (CMD / PowerShell):**

  ```bash
  .\venv\Scripts\activate
  ```

* **macOS / Linux (Bash / Zsh):**

  ```bash
  source venv/bin/activate
  ```

Jika berhasil, di awal baris terminal akan muncul tanda:

```text
(venv) ...
```

Artinya kamu sudah masuk ke “kamar” environment proyek ini.

### 6.4 Menginstall Library yang Dibutuhkan

Dengan venv aktif, install library berikut (contoh untuk proyek Streamlit + LangChain + Google AI):

```bash
pip install streamlit
pip install langchain
pip install langchain_google_genai
pip install google-generativeai
pip install python-dotenv
pip install langchain-core
pip install langchain-community
```

> Semua library ini hanya terinstall di dalam venv proyek ini, bukan global di seluruh komputer.

### 6.5 Menonaktifkan Virtual Environment

Jika sudah selesai bekerja:

```bash
deactivate
```

Prompt terminal akan kembali normal (tanpa `(venv)`).

---

## 7. Troubleshooting

### 7.1 `python` atau `pip` tidak dikenal

Error contoh:

```text
'python' is not recognized as an internal or external command
```

**Solusi:**

* Kemungkinan besar lupa mencentang **"Add Python to PATH"** saat instalasi.
* Ulangi instalasi Python, pastikan opsi **Add to PATH** dicentang.

### 7.2 `streamlit` tidak ditemukan

Error contoh:

```text
streamlit: command not found
```

**Solusi:**

* Pastikan venv **sudah aktif**:

  * Windows: `.\venv\Scripts\activate`
  * macOS/Linux: `source venv/bin/activate`
* Lalu ulangi instalasi:

  ```bash
  pip install streamlit
  ```

---

## 8. Checklist Kesiapan

Sebelum lanjut ke Modul 1, pastikan:

* [ ] Akun Google untuk akses **Google Colab**.
* [ ] **API Key** dari **Google AI Studio** sudah dibuat dan disimpan dengan aman.
* [ ] **VS Code** terinstall dengan ekstensi **Python** aktif.
* [ ] Terminal bisa menjalankan:

  * [ ] `python --version` atau `python3 --version`
  * [ ] `pip --version`
* [ ] Sudah memahami cara:

  * [ ] Membuat folder proyek
  * [ ] Membuat dan mengaktifkan **virtual environment (venv)**
  * [ ] Menginstal library di dalam venv`
