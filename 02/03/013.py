from typing import Optional


class User:
    def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @classmethod
    def with_name(cls, first_name: str, last_name: str):
        return cls(first_name=first_name, last_name=last_name)

    @classmethod
    def with_username(cls, username: str):
        if not cls.is_username_allowed(username):
            raise ValueError('Некорректное имя пользователя')
        return cls(username=username)

    @staticmethod
    def is_username_allowed(username: str):
        return not username.lower().startswith('admin')

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.username:
            return f"@{self.username}"
        else:
            return ""


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
# ne_stas = User.with_username('admin_nestas_anonymous')