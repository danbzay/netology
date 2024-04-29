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

def print_books_by_publisher(session):
    print("\nВведите часть имени или id издателя чтобы увидеть какие изданные"
          + "им книги есть в нашей базе. 'q' для выхода, <Enter> - весь список."
          + "\nСписок издателей:")
    q = session.query(Publisher)
    print('\n'.join(f'id: {_.pk}, Имя: {_.name}' for _ in q.all()))
    while True:
        pub = input()
        if pub == 'q':
            break
        q = session.query(Book, Shop, Sale, Publisher).filter(
                Book.pk == Stock.id_book).filter(
                Shop.pk == Stock.id_shop).filter(
                Sale.id_stock == Stock.pk).filter(
                Publisher.pk == Book.id_publisher).filter(
                    Publisher.pk == int(pub) if pub.isdigit() else
                    Publisher.name.like('%' + pub + '%'))
        print('\n'.join(f'{_[0].title :<40} | {_[1].name :<10} | ' 
              + f'{str(_[2].price) :<8} | {_[2].date_sale.strftime("%d-%m-%Y")}'
              for _ in q.all()))


if __name__ == '__main__':

    DSN = "postgresql://postgres:postgres@localhost:5432/books"
    engine = sq.create_engine(DSN)
    create_tables(engine)

    # сессия
    Session = sessionmaker(bind=engine)
    session = Session()

    #заполняем базу
    json_to_base('tests_data.json', session)

    # Выводим издателя по имени или id
    print_books_by_publisher(session)
    session.close()
