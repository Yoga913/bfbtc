# bfbtc 

bfbtc adalah alat brute force kunci privat bitcoin yang cepat dan efisien yang ditulis dalam bahasa python. 
Alat ini bekerja berdasarkan pembuatan kunci privat acak atau berurutan dan alamat publik terkait.
Kemudian memeriksa alamat tersebut melalui online API atau offline database.
dengan memberikan kontrol atas jumlah inti CPU yang digunakan dan memberikan feedback tentang kecepatan brute force.

Yang membuat bfbtc cepat, terutama adalah pustaka bit-nya.

## **Penginstallan **
```
$ git clone https://github.com/Yoga913/bfbtc.git

$ cd bfbtc

$ pip install -r requirements.txt

$ python bfbtc.py atau $ python3 bfbtc.py di Linux
```

## Tujuan
Tujuan utamanya sepenuhnya projeck ini adalah untuk menganalisa membuktikan bahwa bitcoin aman atau tidak. Setidaknya sampai suatu hari komputer Kuantum mulai bekerja melawannya!


## **Persyaratan**

Dalam mode offline, diperlukan database. Secara default, database tersebut adalah `address.txt` yang berisi beberapa alamat.
Jujur saja, pencarian offline membutuhkan waktu terlalu lama dan alamat dengan saldo yang disertakan dalam program terlalu sedikit (karena memiliki berkas teks terkini dengan semua alamat akan membuat repositori ini lebih dari 5GB).

Jadi pengguna yang ingin mengunduh berkas teks terbaru dari:
[di sini](http://addresses.loyce.club/) (direct [link](http://addresses.loyce.club/Bitcoin_addresses_LATEST.txt.gz)), mengganti nama dan menggantinya dengan "address.txt".
Namun berhati-hatilah dengan masalah memori. Gunakan database ini hanya jika Anda memiliki RAM yang cukup!

### Untuk menginstal persyaratan, jalankan perintah di bawah ini:

```$ pip install -r requirements.txt```

## **Penggunaan**
Cukup jalankan perintah ini: `$ python bfbtc.py` atau `$ python3 bfbtc.py` di Linux, bfbtc memberi tahu Anda apa yang harus dilakukan!

Hasil akan disimpan ke `foundkey.txt` di direktori utama.

## **Note**
Sepenuhnya Saya Tidak Bertanggung Jawab Atas Penyalah Penggunaan Projeck Ini 

