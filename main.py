from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Person():
    def __init__(self, birthday: date, name: str, country: str) -> None:
        self._name: str = name
        self._birthday: date = birthday
        self._country: str = country

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        if value != self._name:
            self._name = value

    @property
    def birthday(self) -> date:
        return self._birthday
    @birthday.setter
    def birthday(self, value:date):
        if value != self._birthday:
            self._birthday = value

    def GetAge(self) -> int:
        now = datetime.now()
        difference = relativedelta(now, self._birthday)
        return difference.years

    @property
    def country(self) -> str:
        return self._country
    @country.setter
    def country(self, value: str):
        if value != self._country:
            self._country = value

mydate = date.fromisoformat('2009-10-02')
myPerson = Person(mydate, 'Felicity', 'America')
myAge = myPerson.GetAge()
print(f'{myPerson.name} is {myAge} years old and lives in {myPerson.country}')


