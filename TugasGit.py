# Program Analisis Data Panen
# Nama: Ahmad Ripai
# NIM: 152024090

data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("="*60)
print("LAPORAN ANALISIS DATA PANEN")
print("="*60)

# 1. Tampilkan seluruh data dari data_panen
print("\n1. SELURUH DATA PANEN:")
print("-"*60)
for lokasi_key, lokasi_data in data_panen.items():
    print(f"\n{lokasi_key.upper()}:")
    print(f"  Nama Lokasi: {lokasi_data['nama_lokasi']}")
    print(f"  Hasil Panen:")
    for tanaman, jumlah in lokasi_data['hasil_panen'].items():
        print(f"    - {tanaman.capitalize()}: {jumlah} kg")

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
print("\n" + "="*60)
print("2. HASIL PANEN JAGUNG LOKASI 2:")
print("-"*60)
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung di {data_panen['lokasi2']['nama_lokasi']}: {jagung_lokasi2} kg")

# 3. Tampilkan nama lokasi dari lokasi3
print("\n" + "="*60)
print("3. NAMA LOKASI 3:")
print("-"*60)
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi3: {nama_lokasi3}")

# 4. Masukkan hasil panen padi dan kedelai ke variabel terpisah
print("\n" + "="*60)
print("4. VARIABEL HASIL PANEN PADI DAN KEDELAI:")
print("-"*60)

# Variabel untuk padi
padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']

# Variabel untuk kedelai
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print("\nPadi per lokasi:")
print(f"  Lokasi 1: {padi_lokasi1} kg")
print(f"  Lokasi 2: {padi_lokasi2} kg")
print(f"  Lokasi 3: {padi_lokasi3} kg")
print(f"  Lokasi 4: {padi_lokasi4} kg")
print(f"  Lokasi 5: {padi_lokasi5} kg")

print("\nKedelai per lokasi:")
print(f"  Lokasi 1: {kedelai_lokasi1} kg")
print(f"  Lokasi 2: {kedelai_lokasi2} kg")
print(f"  Lokasi 3: {kedelai_lokasi3} kg")
print(f"  Lokasi 4: {kedelai_lokasi4} kg")
print(f"  Lokasi 5: {kedelai_lokasi5} kg")

# 5. Percabangan - Analisis kondisi lokasi
print("\n" + "="*60)
print("5. ANALISIS KONDISI LOKASI:")
print("-"*60)

for lokasi_key, lokasi_data in data_panen.items():
    nama = lokasi_data['nama_lokasi']
    padi = lokasi_data['hasil_panen']['padi']
    jagung = lokasi_data['hasil_panen']['jagung']
    
    print(f"\n{nama} ({lokasi_key}):")
    print(f"  Padi: {padi} kg, Jagung: {jagung} kg")
    
    if padi > 1300 or jagung > 800:
        print(f"  Status: ⚠️  MEMERLUKAN PERHATIAN KHUSUS")
        if padi > 1300:
            print(f"    - Padi melebihi 1300 kg ({padi} kg)")
        if jagung > 800:
            print(f"    - Jagung melebihi 800 kg ({jagung} kg)")
    else:
        print(f"  Status: ✓ KONDISI BAIK")

print("="*60)
print("Perubahan pada branch Baru")
print("perubahan")