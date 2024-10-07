class BacteriaProducer:
    def __init__(self, max_bacteria):
        self.max_bacteria = max_bacteria
        self.current_bacteria = 0

    def create_new(self):
        if self.current_bacteria < self.max_bacteria:
            self.current_bacteria += 1
            print(f"Добавлена одна бактерия. Количество бактерий в популяции: {self.current_bacteria}")
        else:
            print("Нет места под новую бактерию")

    def remove_one(self):
        if self.current_bacteria > 0:
            self.current_bacteria -= 1
            print(f"Одна бактерия удалена. Количество бактерий в популяции: {self.current_bacteria}")
        else:
            print("В популяции нет бактерий, удалять нечего")


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()


class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def process_text(self, text, shift, is_encrypt):
        result = ''
        # Если нужно расшифровать, инвертируем сдвиг
        if not is_encrypt:
            shift = -shift
        
        for char in text.lower():
            if char in self.alphabet:
                index = (self.alphabet.index(char) + shift) % len(self.alphabet)
                result += self.alphabet[index]
            else:
                result += char
        return result


# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))