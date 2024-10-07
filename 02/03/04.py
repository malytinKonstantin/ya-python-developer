class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    # Инициализатор класса MobilePhone с новым параметром - network_type.
    def __init__(self, dial_type_value, network_type):
        # Новый атрибут объекта.
        self.network_type = network_type
        # Вызов родительского инициализатора.
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!') 