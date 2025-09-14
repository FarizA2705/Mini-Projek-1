# Mini-Projek-1
Fariz Aufarizky, 2509116004, Sistem Informasi A, Praktikum Dasar-Dasar Pemrograman

Flowchart Sistem Menejemen Pasien Klinik Harapan
<img width="963" height="1152" alt="Screenshot 2025-09-14 004130" src="https://github.com/user-attachments/assets/74b1bb74-7da8-4dc4-ae00-2a5391f841f8" />


Berikut ini adalah penjelesaan tentang program Sistem Menejemen Data Pasien Klinik Harapan

<img width="1415" height="733" alt="Screenshot 2025-09-14 141626" src="https://github.com/user-attachments/assets/2fdf90f9-0d8c-4be7-b607-1a43485ea75d" />
Ini adalah bagian variabel untuk menyimpan data data pasien, karena kita tidak memakai program pengulangan. list_pasien adalah sebuah list yang berisi beberapa dictionary. Setiap dictionary mewakili satu pasien dengan detail seperti ID, data tetap (nama, alamat, usia dalam format tuple), penyakit, diagnosa, dan status.

<img width="2225" height="654" alt="Screenshot 2025-09-14 151337" src="https://github.com/user-attachments/assets/027fd18c-bcd6-4724-a8be-9383861abe74" />
Bagian ini adalah bagian untuk menampilkan semua data data para pasien yang di simpan pada bagian list.

<img width="2560" height="1600" alt="Screenshot 2025-09-14 152007" src="https://github.com/user-attachments/assets/84af5d25-af12-4ddb-9f31-4de039b66b28" />
Yang ketiga adalah Mencari_data bertujuan untuk mencari data pasien secara spesifik, fungsi ini menggunakan logika bercaba seperti if/else, ketika mengetikkan angka 1 akan memmunculkan output "masukkan nama pasien" ketika mengetikkan angka 2 akan muncul output "masukkan ID pasien" dan ketika memasukkan angaka selain 1 dan 2 akan memunculkan output "Pilihan Tidak Valid".

<img width="1185" height="1096" alt="Screenshot 2025-09-14 151239" src="https://github.com/user-attachments/assets/64340c32-7809-43b5-b499-6e66525f448c" />
Selanjutnya ada Tambah_Pasien, untuk menambahkan data pasien user diminta untuk menginput nama,alamat,usia,penyakit,diagnosa,dan status, dan ketika berhasil menambahkan pasien, seharusnya akan membuat id yang baru sepeti 4, tetapi ada kesalahan akibatnya id nya akan diduplikasi seharusnya id menjadi no 4 tetapi malah menjadi 1 dan akan tabrakan dengan id yang sudah ada.

<img width="2560" height="1600" alt="Screenshot 2025-09-14 152811" src="https://github.com/user-attachments/assets/c80c87b0-d12d-4062-89cb-3a2d1ce5444a" />
Dan yang terakhir yaitu Update_Data untuk mengupdate semua data para pasien atau menambahkan suatu penyakit, user diminta untuk menginput id pasien untuk mencari data pasien yang ingin di ubah, user diminta untuk menginput penyakit baru,diagnosis, dan status pasien, ketika berhasil mengupdate data akan muncul output "Data Pasien Berhasil Di update".
