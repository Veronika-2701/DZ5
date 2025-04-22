from address import Address
from mailing import Mailing

m = Mailing(Address(123456, "Obninsk", "Lenina", 12, 3), 
            Address(234567, "Kirov", "Pobedy", 19, 4),
            459, "00876554332213")

print(f"Отправление {m.track} из {m.from_address.index}, {m.from_address.city}, {m.from_address.street}, {m.from_address.home} - {m.from_address.apt} в {m.to_address.index}, {m.to_address.city}, {m.to_address.street}, {m.to_address.home} - {m.to_address.apt}. Стоимость {m.cost} рублей. ")