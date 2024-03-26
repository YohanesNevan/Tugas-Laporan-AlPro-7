namasaya = "Antonius Rachmat C"
temansaya1 = "Yuan Lukito"
temansaya2 = 'Laurentius Kuncoro'
temansaya3 = "Matahari" + 'Bakti'
temansaya4 = "Yohanes" + 'Nevan' + 'AW'

print(temansaya4)
print(temansaya3)
print(namasaya[0]) #'A'
print(namasaya[9]) #'R'
print(temansaya1[1]) #'u'
huruf = temansaya2[0]
print(huruf) #'L'


kalimat = "saya mau makan"
data = "saya"
print(data in kalimat) #True
print("mau" in kalimat) #True
print("dia" in kalimat) #False

if "saya" > "dia":
    print("Ya") #Ya
else:
    print("Tidak")

if "dua" == "dua":
    print("Sama") #Sama
    
kalimat = "universitas kristen duta wacana yogyakarta"
print(len(kalimat)) #output 42

terakhir = kalimat[len(kalimat)-1]
print(terakhir) #output 'a'

#bisa juga menggunakan indeks -1
terakhir_versi2 = kalimat[-1]
print(terakhir_versi2) #output 'a'
#atau menggunakan indeks -2 untuk huruf terakhir kedua
terakhir2 = kalimat[-2]
print(terakhir2) #output 't'

kalimat = "indonesia jaya"
i = 0
while i < len(kalimat):
    print(kalimat[i],end='')
i += 1

kalimat = "cerita rakyat"
awal = 0
akhir = 6
print(kalimat[awal:akhir]) #cerita
print(kalimat[7:len(kalimat)]) #rakyat
print(kalimat[:5]) #cerit
print(kalimat[5:]) #a rakyat
print(kalimat[:]) #cerita rakyat

kata1 = "saya"
kata2 = "makan"
kata3 = kata1 + " " + kata2
print(kata3) #hasil adalah penggabungan: saya makan
kata4 = "ulang"
print(kata4 * 4) #hasil adalah ulangulangulangulang
kata4 = "ulang "
print(kata4 * 2) #hasil adalah ulang ulang

kalimat = "Saudara-saudara, pada tanggal 17-08-1945 Indonesia merdeka"
hasil = kalimat.split(" ")
for kal in hasil:
    if kal[0].isdigit():
        hasil2 = kal.split("-")
        print(hasil2[1]+"/"+hasil2[0]+"/"+hasil2[2])