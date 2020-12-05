#membuat rumus transformasi
#masukkan angka awal
#masukkan rumus transforamsi
#hitung transformasi

def translasi():
    #koordinat awal
    awal_x = int(input("masukkan x: "))
    awal_y = int(input("masukkan y: "))
    print("koordinat awal:",awal_x,",",awal_y)
    #koordinat akhir
    akhir_x = int(input("masukkan x: "))
    akhir_y = int(input("masukkan y: "))
    #hitung dengan rumus
    hitung_x = awal_x + akhir_x
    hitung_y = awal_y + akhir_y
    #koordinat akhir
    total_akhir = print("setelah ditransformasi menjadi",hitung_x,',',hitung_y)

    tanya()
    return total_akhir

def dilatasi():
    #koordinat awal dilatasi
    #dil maksudnya itu dilatasi ya
    dil_awal_x = int(input("masukkan x: "))
    dil_awal_y = int(input("masukkan y: "))
    #skala dilatasi
    dil_skala = int(input("skalanya?: "))
    #hitung rumus
    dil_hitung_x = dil_awal_x * dil_skala
    dil_hitung_y = dil_awal_y * dil_skala
    #total kan
    akhir_dilatasi = print("setelah",dil_awal_x,",",dil_awal_y,"didilatasi dengan",dil_skala,"menjadi",dil_hitung_x,',',dil_hitung_y)
    tanya()
    return akhir_dilatasi

def rotasi():
    #rotasi = rot
    rot_x = int(input("masukkan x: "))
    rot_y = int(input("masukkan y: "))
    print("koordinat awalnya adalah:",rot_x,",",rot_y)
    print("\tpilih rotasi yang diinginkan")
    print("\t1. rotasi terhadap +90°")
    print("\t2. rotasi terhadap -90°")
    print("\t3. rotasi terhadap 180°")
    print("\t4. rotasi terhadap +270°")
    print("\t5. rotasi terhadap -270°")
    #jalankan percabangan
    rotasi_pilihan = input("pilih berdasarkan nomor! ")
    min_num = -(1)
    has_rot_x = rot_x * min_num
    has_rot_y = rot_y * min_num
    if rotasi_pilihan == "1":
        print("setelah dirotasi 90° menjadi",has_rot_y,",",rot_x)
    elif rotasi_pilihan == "2":
        print("setelah dirotasi -90° menjadi",rot_y,',',has_rot_x)
    elif rotasi_pilihan == "3":
        print("setelah dirotasi 180° menjadi",has_rot_x,',',has_rot_y)
    elif rotasi_pilihan == "4":
        print("setelah dirotasi 270° menjadi",rot_y,',',has_rot_x)
    elif rotasi_pilihan == "5":
        print("setelah dirotasi 270° menjadi",has_rot_y,',',rot_x)
    tanya()
    
def refleksi():
    ref_x = int(input("masukkan x: "))
    ref_y = int(input("masukkan y: "))
    print("koordinat awalnya adalah:",ref_x,",",ref_y)
    print("\tpilih refleksi yang diinginkan")
    print("\t1. refleksi terhadap sumbu x")
    print("\t2. refleksi terhadap sumbu y")
    print("\t3. refleksi terhadap sumbu y = x")
    print("\t4. refelksi terhadap sumbu y = -x")
    print("\t5. refleksi terhadap sumbu x = h")
    print("\t6. refleksi terhadap sumbu y = k")
    #masukkan pengubah minus
    #dan juga input
    refleksi_pilihan = input("pilih nomornya aja ")
    min_num = -(1)
    #iya beneran masukin rumusnya
    ref_min_x = ref_x * min_num
    ref_min_y = ref_y * min_num
    if refleksi_pilihan == "1":
        print("setelah direfleksi menjadi",ref_x,',',ref_min_y)
    elif refleksi_pilihan == "2":
        print("setelah direfleksi menjadi",ref_min_x,',',ref_y)
    elif refleksi_pilihan == "3":
        print("setelah direfleksi menjadi",ref_y,',',ref_x)
    elif refleksi_pilihan == "4":
        print("setelah direfleksi menjadi",ref_min_y,',',ref_min_x)
    elif refleksi_pilihan == "5":
        h = int(input("bila x dirubah menjadi: "))
        has_ref_h = ((2*h) - ref_x)
        print("maka setelah direfleksi menjadi",has_ref_h,',',ref_y)
    elif refleksi_pilihan == "6":
        k = int(input("bila x dirubah menjadi: "))
        has_ref_k = ((2*k) - ref_y)
        print("maka setelah direfleksi menjadi",ref_x,',',has_ref_k)
        
    tanya()
        


def hitung():
    print('\n\t=============================')
    print('\tProgram transforamsi dan dilatasi')
    print('\t===============================')
    print('\t1. translasi')
    print('\t2. dilatasi')
    print("\t3. rotasi")
    print("\t4. refleksi")
    print('\t===============================')
    print('\tSilahkan pilih 1-3')
    print('') 

def pilihan():
    pilih = input("Pilih translasi,dilatasi,rotasi atau refleksi? ")
    #meminta input dari user
    if pilih == "translasi":
        translasi()
    elif pilih == "dilatasi":
        dilatasi()
    elif pilih == "rotasi":
        rotasi()
    elif pilih == "refleksi":
        refleksi()
    else:
        print("ga ada pilihan",pilih)
    

def tanya():
    tanya = input("\n\tKembali ke menu kalkulator? (y/t)?")
    if tanya == "y":
        pilihan()
    elif tanya == "t":
        print("terima kasih telah menggunakan kalkulator yang kubuat :)")
        exit
    else:
        print("ga ada pilihan itu hehe")


hitung()
pilihan()







