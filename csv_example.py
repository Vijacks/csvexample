import csv

from matplotlib import pyplot as plt

sayi1 = 0
sayi2 = 0
sayi3 = 0
TotalPowerConsumption1 = 0
TotalPowerConsumption2 = 0
TotalPowerConsumption3 = 0
with open("powerconsumption.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for Datetime, Temperature, Humidity, WindSpeed, GeneralDiffuseFlows, DiffuseFlows, PowerConsumption_Zone1, PowerConsumption_Zone2, PowerConsumption_Zone3 in reader:
        if PowerConsumption_Zone1:
            sayi1 += 1
            TotalPowerConsumption1 += float(PowerConsumption_Zone1)
        if PowerConsumption_Zone2:
            sayi2 += 1
            TotalPowerConsumption2 += float(PowerConsumption_Zone2)
        if PowerConsumption_Zone3:
            sayi3 += 1
            TotalPowerConsumption3 += float(PowerConsumption_Zone3)
BölgeOrtalama1 = TotalPowerConsumption1 / sayi1
BölgeOrtalama2 = TotalPowerConsumption2 / sayi2
BölgeOrtalama3 = TotalPowerConsumption3 / sayi3
print(f"Birinci bölgedeki toplam enerji, {TotalPowerConsumption1}")
print(f"Birinci bölgedeki ortalama enerji, {BölgeOrtalama1}")
print(f"İkinci bölgedeki toplam enerji, {TotalPowerConsumption2}")
print(f"İkinci bölgedeki ortalama enerji, {BölgeOrtalama2}")
print(f"Üçüncü bölgedeki toplam enerji, {TotalPowerConsumption3}")
print(f"Üçüncü bölgedeki ortalama enerji, {BölgeOrtalama3}")
bölgeler = ["Bölge 1", "Bölge 2", "Bölge 3"]
OrtalamaDegerler = [BölgeOrtalama1, BölgeOrtalama2, BölgeOrtalama3]
plt.figure(figsize=(8, 8))
plt.bar(bölgeler, OrtalamaDegerler, color=["skyblue", "salmon", "lightgreen"])
plt.ylabel("Ortalama Enerji Tüketimi")
plt.title("Bölgelerin Ortalama Enerji Tüketimi")
plt.show()
