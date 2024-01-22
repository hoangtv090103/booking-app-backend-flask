from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True)
    username = Column(String(50), unique=True)
    password = Column(String(120), unique=True)
    user = relationship('User', backref='account', uselist=False)

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def __repr__(self):
        return f'<Account {self.username!r}>'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    account_id = Column(Integer, ForeignKey('account.id'), unique=True)

    def __init__(self, name=None, email=None, account_id=None):
        self.name = name
        self.email = email
        self.account_id = account_id

    def __repr__(self):
        return f'<User {self.name!r}>'
