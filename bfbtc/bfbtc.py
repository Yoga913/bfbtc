import requests
from bit import Key
from time import sleep, time
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

if os.path.exists(os.getcwd()+"/cache.txt") == False:
    open("cache.txt", "w+")

# 1. **Impor Modul dan Penyiapan**: Program mengimpor modul-modul yang diperlukan seperti `requests`, `bit`, dan modul bawaan Python seperti `os`, `threading`, dan `concurrent.futures`.
#  Program juga memeriksa apakah file `cache.txt` ada, jika tidak, maka file tersebut akan dibuat.

class bfbtc():
    def __init__(self):
        self.start_t = 0
        self.prev_n = 0
        self.cur_n = 0
        self.start_n = 0
        self.end_n = 0
        self.seq = False
        self.privateKey = None
        self.start_r = 0
        loaded_addresses = open("address.txt", "r").readlines()
        loaded_addresses = [x.rstrip() for x in loaded_addresses]
        # Remove invalid wallet addresses
        loaded_addresses = [x for x in loaded_addresses if x.find('wallet') == -1 and len(x) > 0]
        self.loaded_addresses = set(loaded_addresses)

    # 2. **Kelas bfbtc**: Program mendefinisikan kelas `bfbtc` yang memiliki beberapa metode untuk melakukan brute force, memeriksa kecepatan, dan mengatur input pengguna.
   
    def speed(self):
        while True:
            if self.cur_n != 0:
                cur_t = time()
                n = self.cur_n
                if self.prev_n == 0:
                    self.prev_n = n
                elapsed_t=cur_t-self.start_t
                print("Kewargaan Saat ini: "+str(n)+", Nilai Tukar Saat Ini: "+str(abs(n-self.prev_n)//2)+"/s"+f", Waktu Berlalu: [{str(elapsed_t//3600)[:-2]}:{str(elapsed_t//60%60)[:-2]}:{int(elapsed_t%60)}], total: {n-self.start_r} ", end="\r")
                self.prev_n = n
                if self.seq:
                    open("cache.txt","w").write(f"{self.cur_n}-{self.start_r}-{self.end_n}")
            sleep(2)
    
    # 3. **Metode `speed`**: Metode ini akan terus-menerus mencetak kecepatan brute force ke layar, menunjukkan jumlah iterasi yang telah dilakukan per detik, dan waktu total yang telah berlalu.

    def random_brute(self, n):
        self.cur_n=n
        key = Key()
        if key.address in self.loaded_addresses:
                print("Alamat Yang Cocok Ditemukan!")
                print("Public Adress: "+key.address)
                print("Private Key: "+key.to_wif())
                f = open("foundkey.txt", "a") # kunci pribadi dan alamat yang ditemukan disimpan ke "foundkey.txt"
                f.write(key.address+"\n")
                f.write(key.to_wif()+"\n")
                f.close()
                sleep(510)
                exit()
    
    # 4. **Metode `random_brute`**: Metode ini menghasilkan kunci privat secara acak dan memeriksa apakah alamat Bitcoin yang dihasilkan ada di dalam daftar alamat yang dimuat sebelumnya.
    #  Jika ada, kunci privat dan alamat publik akan dicetak dan disimpan dalam file `foundkey.txt`.
        
    def sequential_brute(self, n):
        self.cur_n=n
        key = Key().from_int(n)
        if key.address in self.loaded_addresses:
            print("Alamat Yang Cocok ditemukan!")
            print("Public Adress: "+key.address)
            print("Private Key: "+key.to_wif())
            f = open("foundkey.txt", "a") # kunci pribadi dan alamat yang ditemukan disimpan ke "foundkey.txt"
            f.write(key.address+"\n")
            f.write(key.to_wif()+"\n")
            f.close()
            sleep(500)
            exit()

    # 5. **Metode `sequential_brute`**: Metode ini melakukan brute force secara berurutan terhadap kunci privat.
    #  Ini juga memeriksa apakah alamat Bitcoin yang dihasilkan ada di dalam daftar alamat yang dimuat sebelumnya.

    
    def random_online_brute(self, n):
        self.cur_n = n
        key = Key()
        the_page = requests.get("https://blockchain.info/q/getreceivedbyaddress/"+key.address+"/").text
        if int(the_page)>0:
            print(the_page)
            print("Alamat Aktif Di temukan!")
            print(key.address)
            print(key.to_wif())
            f = open("foundkey.txt", "a") # kunci pribadi dan alamat yang ditemukan disimpan ke "foundkey.txt"
            f.write(key.address+"\n")
            f.write(key.to_wif()+"\n")
            f.close()
            sleep(500)
            exit()

    # 6. **Metode `random_online_brute`**: Metode ini melakukan brute force secara acak secara online dengan mengirim permintaan ke server blockchain.
    # info untuk memeriksa saldo alamat Bitcoin yang dihasilkan. Jika alamat tersebut memiliki saldo lebih besar dari 0, maka kunci privat dan alamat publik akan dicetak dan disimpan dalam file `foundkey.txt`.
            
    def num_of_cores(self):
        available_cores = cpu_count()
        cores = input(f"\nJumlah inti yang tersedia: {available_cores}\n \n Berapa banyak inti yang akan digunakan? (biarkan kosong untuk menggunakan semua inti yang tersedia) \n \n Ketik sesuatu>")
        if cores == "":
            self.cores = int(available_cores)
        elif cores.isdigit():
            cores = int(cores)
            if 0 < cores <= available_cores:
                self.cores = cores
            elif cores<=0 :
                print(f"Hei kamu tidak bisa menggunakannya {cores} jumlah inti CPU!")
                input("Tekan Enter untuk keluar")
                raise ValueError("Angka Negatif!")
            elif cores > available_cores:
                print(f"\n Kamu Hanya Punya {available_cores} inti")
                print(f" Apakah Anda yakin ingin menggunakan {cores} inti?")
                core_input = input("\n[y]a atau [t]idak>")
                if core_input == "y":
                    self.cores = cores
                else:
                    print("menggunakan jumlah inti yang tersedia")
                    self.cores = available_cores
        else:
            print("Masukan Salah!")
            input("Tekan Enter untuk keluar")
            exit()

    # 7. **Metode `num_of_cores`**: Metode ini digunakan untuk memperoleh jumlah inti CPU yang tersedia dan meminta pengguna untuk memilih berapa banyak inti CPU yang ingin digunakan untuk brute force.
        
    def generate_random_address(self):
        key = Key()
        print("\n Public Address: "+key.address)
        print(" Private Key: "+key.to_wif())
    
    # 8. **Metode `generate_random_address` dan `generate_address_fromKey`**: Metode ini menghasilkan pasangan kunci publik-privat secara acak atau dari kunci privat yang diberikan oleh pengguna.

    def generate_address_fromKey(self):
        if self.privateKey != "":
            key = Key(self.privateKey)
            print("\n Public Address: "+key.address)
            print("\n Dompet Anda sudah siap!")
        else:
            print("Dilarang masuk")

    # 9. **Metode `get_user_input`**: Metode ini meminta input dari pengguna untuk memilih tindakan yang ingin dilakukan, seperti menghasilkan kunci acak, melakukan brute force offline atau online, atau keluar dari program.
        
    def get_user_input(self):
        user_input = input("\n Apa yang ingin kamu lakukan? \n \n   [1]: menghasilkan pasangan kunci acak \n [2]: menghasilkan alamat publik dari kunci pribadi \n [3]: brute force bitcoin mode offline \n [4]: ​​brute force bitcoin mode online \n [0]: keluar \n \n Ketik sesuatu>")
        if user_input == "1":
            self.generate_random_address()
            print("\n Dompet Anda sudah siap!")
            input("\n Tekan Enter untuk keluar")
            exit()
        elif user_input == "2":
            self.privateKey = input("\n Enter Private Key>")
            try:
                self.generate_address_fromKey()
            except:
                print("\n format kunci salah")
            input("Tekan Enter untuk keluar")
            exit()
        elif user_input == "3":
            method_input = input(" \n Masukkan nomor yang diinginkan: \n \n [1]: serangan acak \n [2]: serangan berurutan \n [0]: keluar \n \n Ketik sesuatu>")
            if method_input=="1":
                target = self.random_brute
            elif method_input=="2":
                if open("cache.txt", "r").read() != "":
                    r0=open("cache.txt").read().split("-")
                    print(f"rentang resume {r0[0]}-{r0[2]}")
                    with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                        print("\nMelanjutkan ...\n")
                        self.start_t = time()
                        self.start_r = int(r0[1])
                        self.start_n = int(r0[0])
                        self.end_n = int(r0[2])
                        self.seq=True
                        for i in range(self.start_n,self.end_n):
                            pool.submit(self.sequential_brute, i)
                        print("Berhenti\n")
                        exit()
                else:
                    range0 = input("\n Masukkan rentang dalam desimal (contoh:1-100)>")
                    r0 = range0.split("-")
                    r0.insert(1,r0[0])
                    open("cache.txt", "w").write("-".join(r0))
                    with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                        print("\n memulai ...")
                        self.start_t = time()
                        self.start_r = int(r0[1])
                        self.start_n = int(r0[0])
                        self.end_n = int(r0[2])
                        self.seq=True
                        for i in range(self.start_n,self.end_n):
                            pool.submit(self.sequential_brute, i)
                        print("Berhenti\n")
                        exit()
            else:
                print("Keluar...")
                exit()
        elif user_input == "4":
            method_input = input(" \n Masukkan nomor yang diinginkan: \n \n [1]: serangan acak \n [2]: serangan berurutan \n [0]: keluar \n \n Ketik sesuatu>")
            if method_input=="1":
                with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                    r = range(100000000000000000)
                    print("\n Memulai...")
                    self.start_t = time()
                    self.start_n = 0
                    for i in r:
                        pool.submit(self.random_online_brute, i)
                        sleep(0.1)
                    print("Berhenti\n")
                    exit()
            elif method_input=="2":
                print("serangan daring berurutan akan segera tersedia!")
                input("Tekan Enter untuk keluar")
                exit()
            else:
                print("Keluar...")
                exit()
        elif user_input == "0":
            print("Keluar")
            sleep(2)
            exit()
        else:
            print("Tidak ada masukan. <1> dipilih secara otomatis")
            self.generate_random_address()
            print("Dompet Anda sudah siap!")
            input("Tekan Enter untuk keluar")
            exit()
        with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
            r = range(100000000000000000)
            print("\n Memulai...")
            self.start_t = time()
            self.start_n = 0
            for i in r:
                pool.submit(target, i)
            print("Berhenti\n")
            exit()

    # 10. **Penanganan Input Pengguna**: Program menangani input pengguna dan memanggil metode yang sesuai berdasarkan pilihan pengguna.


if __name__ =="__main__":
        obj = bfbtc()
        try:
            t0 = threading.Thread(target=obj.get_user_input)
            t1 = threading.Thread(target=obj.speed)
            t1.daemon = True
            t0.daemon = True
            t0.start()
            t1.start()
            sleep(4000000) # stay in the `try..except`
            sleep(4000000) # stay in the `try..except`
        except KeyboardInterrupt:
            print("\n\n Tekan Ctrl+C. \nKeluar...")
            exit()
        else:
            print(f"\n\nError: {Exception.args}\n")
            exit()

    # 11. **Eksekusi Program**: Program membuat objek dari kelas `bfbtc` dan memulai dua thread: satu untuk menerima input pengguna dan satu lagi untuk memantau kecepatan brute force.
    #  Program juga menangani pengecualian seperti jika pengguna menekan Ctrl+C atau jika terjadi kesalahan selama eksekusi.
