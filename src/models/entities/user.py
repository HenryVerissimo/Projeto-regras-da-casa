from datetime import date, datetime

class User:

    def __init__(self, name: str, email: str, password: int, birth_date: str) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.birth_date = birth_date

    @property
    def email(self) -> None:
        return self.name
    
    @email.setter
    def email(self, email) -> None:
        if isinstance(email, str) and email.count("@") == 1:

            # if verificar se o email existe no banco

            self._email = email

        else: raise Exception("Email inválido!")


    @property
    def age(self) -> int:

        current_date = date.today()
        birth_date = datetime.strptime(self.birth_date, '%d/%m/%Y')
        user_age = current_date.year - birth_date.year

        if current_date.month ==  birth_date.month and current_date.day < birth_date.day: return user_age - 1

        elif current_date.month < birth_date.month: return user_age - 1
        
        else: return user_age
    