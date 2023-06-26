# Minimum Spanning Tree Visualizer
<h2 align="center">
   MST-Visualizer
</h2>
<hr>

## Table of Contents
1. [General Info](#general-information)
2. [Creator Info](#creator-information)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup](#setup)
6. [Usage](#usage)
7. [Video Capture](#videocapture)
8. [Screenshots](#screenshots)
9. [Structure](#structure)
10. [Project Status](#project-status)
11. [Room for Improvement](#room-for-improvement)
12. [Acknowledgements](#acknowledgements)
13. [Contact](#contact)

<a name="general-information"></a>

## General Information
Sebuah aplikasi berbasis GUI (Graphical User Interface) sederhana yang dapat digunakan untuk melakukan visualisasi serta perhitungan minimum spanning tree menggunakan algoritma prim dan kruskal. Program ini juga dapat digunakan untuk membagi graf yang diberikan berdasarkan masukan nilai n dari user. Selain itu, terdapat fitur untuk menambah dan menghapus node dalam graf. Aplikasi ini disusun menggunakan bahasa python serta library tkinter. Tugas ini disusun untuk memenuhi tugas kedua seleksi Lab IRK tahun 2023.
 
<a name="creator-information"></a>

## Creator Information

| Nama                        | NIM      | E-Mail                      |
| --------------------------- | -------- | --------------------------- |
| Mohammad Rifqi Farhansyah   | 13521166 | 13521166@std.stei.itb.ac.id |

<a name="features"></a>

## Features
- Memilih `algoritma` yang akan digunakan
- Membuka `file config` yang berisi bobot dari graf
- `Menambah` dan `menghapus` node dalam graf
- Melakukan `visualisasi` graf menggunakan algoritma prim atau kruskal
- Melakukan `perhitungan` minimum spanning tree menggunakan algoritma prim atau kruskal
- Melakukan `proses n-clustering` graf berdasarkan masukan nilai n dari user

<a name="technologies-used"></a>

## Technologies Used
- Tkinter - version 8.6

> Note: The version of the libraries above is the version that we used in this project. You can use the latest version of the libraries.

<a name="setup"></a>

## Setup
1. Clone Repository ini dengan menggunakan command berikut
   ```sh
   git clone https://github.com/rifqifarhansyah/MST-Visualizer.git
   ```
2. Buka Folder "MST-Visualizer" yang telah di-clone
3. Buka terminal pada direktori tersebut
4. Masuk ke direktori src dengan menggunakan command berikut
   ```sh
   cd src
   ```
5. Jalankan command berikut untuk menjalankan program
   ```sh
   python3 main.py
   ```

<a name="usage"></a>

## Usage
1. Pilih `algoritma` yang akan digunakan dengan mengklik tombol `Prim` atau `Kruskal`
2. Pilih `file config` yang berisi bobot dari graf dengan mengklik tombol `Open File`
3. Jika ingin `menambah atau menghapus node`, isi bagian yang diperlukan, lalu tekan tombol terkait
4. Jika ingin melakukan visualisasi graf, klik tombol `Solve`
5. Apabila hendak melakukan `n-clustering`, isi nilai n yang diinginkan, lalu tekan tombol `Set Clusters`

<a name="videocapture"></a>

## Video Capture
<nl>

![MST-Clustering Gif](https://github.com/rifqifarhansyah/MST-Visualizer/blob/main/img/MST.gif?raw=true)

<a name="screenshots"></a>

## Screenshots
<p>
  <p>Gambar 1. Landing Page</p>
  <img src="/img/SS1.png/">
  <nl>
  <p>Gambar 2. Visualisasi Graf</p>
  <img src="/img/SS2.png/">
  <nl>
  <p>Gambar 3. Visualisasi MST</p>
  <img src="/img/SS3.png/">
  <nl>
   <p>Gambar 4. N-Clustering</p>
   <img src="/img/SS4.png/">
   <nl>
</p>

<a name="structure"></a>

## Structure
```bash
│   README.md
│
├───data
│       config.txt
│
├───img
│       MST.gif
│       SS1.png
│       SS2.png
│       SS3.png
│       SS4.png
│
└───src
        icon.png
        main.py
```

<a name="project-status">

## Project Status
Project is: _complete_

<a name="room-for-improvement">

## Room for Improvement
Perbaikan yang dapat dilakukan pada program ini adalah:
- Menambahkan fungsionalitas lainnya

<a name="acknowledgements">

## Acknowledgements
- Terima kasih kepada Tuhan Yang Maha Esa

<a name="contact"></a>

## Contact
<h4 align="center">
  Kontak Saya : mrifki193@gmail.com<br/>
  2023
</h4>
<hr>
