from smartphone import Smartphone

catalog = Smartphone

catalog = [
    Smartphone("Poco", "F3", "89190398008"), 
    Smartphone("Iphone", "15 Pro Max", "89123456677"),
    Smartphone("Samsung", "A5", "89190546789"),
    Smartphone("Xiaomi", "14 Pro", "89123456789"),
    Smartphone("GooglePixle", "8 Pro", "89154637289")
]

for smartphone in catalog:
    print(f"{smartphone.marka_phone} - {smartphone.model_phone}. {smartphone.num_phone}")