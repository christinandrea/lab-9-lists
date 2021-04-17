#Christina Andrea Putri - Universitas Kristen Duta Wacana

# Shefira membuat aplikasi sederhana yang berfungsi untuk menginput data. Ia memanfaatkan ini untuk menginput barang-barang pribadinya.
# Ia berharap outputnya akan mengurutkan barang-barangnya sesuai dengan urutan A-Z. 


#Input : jumlah data, nama barangnya
#Proses : pengurutan data-datanya 
#Output : data barang-barang yang sudah diinput

try : 
    emp = []
    range_num = int(input("Masukkan jumlah data : "))
    for i in range(range_num):
        inpdata = input("Data %d : "%(i+1))
        emp.append(inpdata)
    
    inpagain = input("Apakah Anda masih ingin melanjutkan? (Ya/Tidak) : ")

    while inpagain=="Ya" or inpagain=="ya":
        range_num = int(input("Masukkan jumlah data : "))
        for i in range(range_num):
            inpdata = input("Data %d : "%(i+1))
            emp.append(inpdata)
            emp.sort()
        inpagain = input("Apakah Anda masih ingin melanjutkan? (Ya/Tidak) : ")
    else : 
        print("Data Anda berhasil diinput. ")
        print("Berikut adalah data Anda: ")
        for items in emp:
            print(items)

except:
    print("Invalid input. Try Again")

