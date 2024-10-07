class Employee:
    """Класс сотрудника с атрибутами для системы учёта отпусков."""
    
    vacation_days = 28  # Количество дней отпуска по умолчанию

    def __init__(self, first_name: str, second_name: str, gender: str):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender

    def __str__(self):
        return (f"Имя: {self.first_name}, Фамилия: {self.second_name}, "
                f"Пол: {self.gender}, Отпускных дней в году: {self.vacation_days}")


# Создаем экземпляры класса Employee с различными значениями атрибутов
employee1 = Employee("Роберт", "Крузо", "м")
employee2 = Employee("Анна", "Каренина", "ж")

# Выводим информацию о сотрудниках
print(employee1)
print(employee2)