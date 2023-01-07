from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    address: str
    gender: str
    birth_year: str
    birth_month: str
    birth_day: int
    subject: str
    hobby: str
    avatar: str
    state: str
    city: str


alla = User(first_name='Alla',
            last_name='Alekhina',
            email='allaale@gmail.com',
            mobile='7931667893',
            address='India',
            gender='Female',
            birth_year='1992',
            birth_month='April',
            birth_day=10,
            subject='Arts',
            hobby='Sports',
            avatar='pic.jpg',
            state='Uttar Pradesh',
            city='Agra')
