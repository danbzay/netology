import sqlalchemy as sq
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    pk = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


class Book(Base):
    __tablename__ = "book"

    pk = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=255))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.pk"))

    publisher = relationship(Publisher, backref="book")

class Shop(Base):
    __tablename__ = "shop"

    pk = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=255))


class Stock(Base):
    __tablename__ = "stock"

    pk = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.pk"))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.pk"))
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")
    

class Sale(Base):
    __tablename__ = "sale"

    pk = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric(scale=2))
    date_sale = sq.Column(sq.Date())
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.pk"))
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref="sale")
    
def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def json_to_base(filename, session):
    if session.query(Publisher).first():
        return
    with open(filename) as f:
        data = json.load(f)
        base_data=[]
    for _ in data:
        bd = globals()[_['model'].capitalize()]()
        bd.pk = _["pk"]
        for k,v, in _["fields"].items():
            setattr(bd, k, v)
        base_data.append(bd)
    session.add_all(base_data)
    session.commit()



DSN = "postgresql://postgres:postgres@localhost:5432/books"
engine = sq.create_engine(DSN)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

#заполняем базу
json_to_base('tests_data.json', session)

print('Введите издателя, или его часть, но в наличии только такие:')
q = session.query(Publisher)
print(', '.join(_.name for _ in q.all()))
pub = input()
# print(b.name
q = session.query(Book, Shop, Sale, Publisher).filter(
        Book.pk == Stock.id_book).filter(
        Shop.pk == Stock.id_shop).filter(
        Sale.id_stock == Stock.pk).filter(
        Publisher.pk == Book.id_publisher).filter(
        Publisher.name.like('%' + pub + '%'))
print('\n'.join(_[0].title + ' | ' + _[1].name + ' | ' + str(_[2].price) 
    + ' | ' + str(_[2].date_sale) for _ in q.all()))
session.close()
