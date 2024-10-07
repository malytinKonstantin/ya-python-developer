class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        """Списывает указанное количество дней отпуска."""
        if days > self.remaining_vacation_days:
            print(f"Ошибка: у сотрудника осталось только {self.remaining_vacation_days} дней отпуска.")
        else:
            self.remaining_vacation_days -= days
            print(f"Использовано {days} дней отпуска.")

    def get_vacation_details(self):
        """Возвращает информацию об оставшихся днях отпуска."""
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."

# Пример использования класса:
employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())