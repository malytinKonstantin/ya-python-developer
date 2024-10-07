from decimal import Decimal
from datetime import datetime, date, timedelta
from typing import Dict, List, Tuple, Optional, Union

DATE_FORMAT = '%Y-%m-%d'

goods: Dict[str, List[Dict[str, Union[Decimal, Optional[date]]]]] = {}

def add(
    items: Dict[str, List[Dict[str, Union[Decimal, Optional[date]]]]],
    title: str,
    quantity: int | float | str,
    expiration_date: Optional[str | date] = None
) -> None:
    """
    Добавляет товар в список продуктов.

    Args:
        items: Словарь с товарами.
        title: Название товара.
        quantity: Количество товара.
        expiration_date: Дата истечения срока годности (опционально).
    """
    if title not in items:
        items[title] = []

    if isinstance(expiration_date, str):
        expiration_date = datetime.strptime(
            expiration_date, DATE_FORMAT
        ).date()

    items[title].append({
        'amount': Decimal(str(quantity)),
        'expiration_date': expiration_date
    })

def add_by_note(items: Dict[str, List[Dict[str, Union[Decimal, Optional[date]]]]], 
                note: str) -> None:
    """
    Добавляет товар в список продуктов по заметке.

    Args:
        items: Словарь с товарами.
        note: Заметка с информацией о товаре.
    """
    parts = note.split()
    date_str = None
    if len(parts) > 2 and '-' in parts[-1]:
        date_str = parts[-1]
    
    if date_str:
        expiration_date = datetime.strptime(date_str, DATE_FORMAT).date()
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])
    
    add(items, title, amount, expiration_date)

def find(items: Dict[str, List[Dict[str, Union[Decimal, Optional[date]]]]], 
         needle: str) -> List[str]:
    """
    Ищет товары по части названия.

    Args:
        items: Словарь с товарами.
        needle: Часть названия для поиска.

    Returns:
        Список найденных товаров.
    """
    found_items = []
    for title in items.keys():
        if needle.lower() in title.lower():
            found_items.append(title)
    return found_items

def amount(items: Dict[str, List[Dict[str, Union[Decimal, Optional[date]]]]], 
           needle: str) -> Decimal:
    """
    Вычисляет общее количество товара по части названия.

    Args:
        items: Словарь с товарами.
        needle: Часть названия для поиска.

    Returns:
        Общее количество найденного товара.
    """
    found_items = find(items, needle)
    total_amount = Decimal('0')
    for title in found_items:
        for batch in items[title]:
            total_amount += Decimal(str(batch['amount']))
    if total_amount == 0:
        return Decimal('0')
    else:
        return total_amount

def expire(items: Dict[str, List[Dict[str, Union[Decimal, Optional[date]]]]], 
           in_advance_days: int = 0) -> List[Tuple[str, Decimal]]:
    """
    Находит просроченные товары.
    Args:
        items: Словарь с товарами.
        in_advance_days: Количество дней для предварительной проверки (по умолчанию 0).

    Returns:
        Список кортежей с названием товара и количеством просроченного товара.
    """
    today = date.today()
    expiration_date = today + timedelta(days=in_advance_days)
    expired = []
    
    for title, batches in items.items():
        total_expired = Decimal('0')
        for batch in batches:
            if batch['expiration_date'] and batch['expiration_date'] <= expiration_date:
                total_expired += Decimal(str(batch['amount']))
        
        if total_expired > 0:
            expired.append((title, total_expired))
    
    return expired

# Пример использования:
add(goods, 'Молоко', 1, '2023-07-20')
add(goods, 'Хлеб', 0.5, '2023-07-15')
add_by_note(goods, 'Сыр 0.3 2023-07-25')
print(find(goods, 'мол'))
print(amount(goods, 'Молоко'))
print(expire(goods, 5))
