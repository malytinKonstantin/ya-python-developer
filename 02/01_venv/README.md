# Создание и активация виртуального окружения
python3 -m venv venv
source ./venv/bin/activate

# Установка зависимостей из файла requirements.txt
pip install -r requirements.txt

# Установка pytest
python3 -m pip install pytest

# Обновление pip до последней версии
python3 -m pip install --upgrade pip 

# Просмотр списка установленных пакетов
python3 -m pip list   

# Сохранение списка зависимостей в файл
pip freeze > requirements.txt 

# Запуск тестов с помощью pytest
pytest

# Деактивация виртуального окружения
deactivate

# Дополнительные команды

# Создание файла practicum.py
touch practicum.py

# Редактирование файла practicum.py (пример с использованием nano)
nano practicum.py

# Запуск скрипта
python practicum.py


which python3

git log
git show
git reset HEAD