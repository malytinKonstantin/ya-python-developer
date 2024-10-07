from datetime import datetime

class Store:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        return False

    def get_info(self, date_str):
        date_object = datetime.strptime(date_str, '%d.%m.%Y')
        
        if self.is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


class MiniStore(Store):
    def is_open(self, date):
        return date.weekday() < 5  # 0-4 это пн-пт


class WeekendStore(Store):
    def is_open(self, date):
        return date.weekday() >= 5  # 5-6 это сб-вс


class NonStopStore(Store):
    def is_open(self, date):
        return True  # Всегда открыт


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))