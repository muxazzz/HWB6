import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import server_sql

DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

def number(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums_cnt = session.query(Album).filter(Album.artist == artist).count()
    
    return albums_cnt



def save(user_data, user_data1, user_data2, user_data3):
    session = connect_db()
    albums_exist = session.query(Album).filter(Album.artist == user_data).count()
    if albums_exist != 0:
        print("Альбом уже существует")
    else:
        total_cnt = session.query(Album).count()
        artist = Album(id=total_cnt+1, year=user_data2,artist=user_data,genre=user_data1,album=user_data3)
        session.add(artist)
        session.commit()
        print("неверное значение")
    return albums_exist
    