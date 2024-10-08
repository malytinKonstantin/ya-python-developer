Основные правила PEP 8
=======================

1. Длина строки:
   - Не должна превышать 79 символов.

2. Отступы:
   - Вложенные блоки кода — 4 пробела.

3. Именование:
   - Стиль именования переменных и функций соответствует разделу PEP 8: Naming Conventions.

4. Перенос строк:
   - Необходимо следовать правилам отступов.
   - Не рекомендуется применять бэкслеши \ для переноса строк.

5. Импорты:
   - Не должно быть неиспользуемых импортов.
   - Порядок импортов:
     1. Импорты из стандартной библиотеки.
     2. Импорты из сторонних библиотек.
   - Внутри каждой группы импорты сортируются в алфавитном порядке.

6. Функции верхнего уровня:
   - Должны разделяться двумя пустыми строками.

7. Кавычки:
   - Применяются кавычки одного типа: либо одинарные, либо двойные.
   - В Практикуме применяются одинарные кавычки.

8. Комментарии:
   - Начинаются со знака #, отделенного одним пробелом от текста.
   - Выравниваются с кодом, к которому относятся.
   - Если в той же строке, что и код — два пробела между кодом и комментарием.
   - Начинаются с заглавной буквы и заканчиваются точкой.
   - Не должны превышать 72 символа.

Правила оформления кода в Практикуме
====================================

1. Имена переменных:
   - Не должны состоять из одной буквы (за редкими исключениями).
   - Не должны содержать названия типа данных.
   - Должны быть осмысленными и на английском языке.

2. Кавычки:
   - Первого уровня — одинарные.
   - Вложенные — двойные.

Примеры:
- Правильно: quotes_rule = 'Строку обрамляем одинарными кавычками!'
- Правильно: nested_quotes_rule = 'В качестве вложенных кавычек применяем "dumb quotes" - двойные верхние кавычки'
- Неправильно: month_name_str = 'Май'
- Неправильно: days_tuple = ('Понедельник', 'Среда')
- Неправильно: vykhodnye = ['Суббота', 'Воскресенье']
