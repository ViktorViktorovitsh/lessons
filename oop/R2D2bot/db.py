from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base() 
# создаем объект класса Engine (диалект://log:passwd@url:port/db_name)
engine = create_engine('Путь к Ваше БД') 
Session = sessionmaker(bind=engine)  # Создаем фабрику для создания экземпляров Session
session = Session()  # Создаем объект сессии из вышесозданной фабрики Session


# Таблица с данными пользователя
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    vk_id = Column(Integer, unique = True)
    first_name = Column(String)
    last_name = Column(String)
    range_age = Column(String)
    city = Column(String)



# Таблица сохраненных юзеров
class DatingUser(Base):
    __tablename__ = 'datinguser'
    id = Column(Integer, primary_key=True)
    vk_id = Column(Integer)       # id юзера-половинки
    first_name = Column(String)   # имя
    last_name = Column(String)    # фамилия
    id_User = Column(Integer, ForeignKey('user.id')) # 
    Like = Column(Boolean)
    user = relationship(User)


# Создать пустые таблицы в БД 
def create_tables():
    Base.metadata.create_all(engine)  # Метод create_all создает таблицы в БД (если они не сущ-т), определенные с помощью  DeclarativeBase (Base)


# Добавляем пользователя в БД
def add_user(user):
    session.expire_on_commit = False  # По умолчанию True, тогда все экземпляры будут полностью просрочены после каждого commit()
    session.add(user)  # добавление объекта в сессию
    session.commit()  # применяем все изменения в базу данных и фиксируем все транзакции



# Показать сохраненных юзеров из БД
def view_all(user_id):
    links = []
    id_query = session.query(User.id).order_by(User.id.desc()).filter(User.vk_id == user_id).limit(1)
    id_list = [p.id for p in id_query]
    id_user = id_list[0]
    # Показываем только тех, кого лайкнули
    dating_users_query = session.query(DatingUser.vk_id).filter(DatingUser.id_User == id_user, DatingUser.Like == True).all()
    dating_users_list = [du.vk_id for du in dating_users_query]
    for link in dating_users_list:
        links.append(link)
    return links

# проверяем наличие пользователя в базе
def check(user_id):
    vk_id_query = session.query(User)
    vk_id_list = [i.vk_id for i in vk_id_query]
    if user_id in vk_id_list:
        vk_id_query = session.query(User).filter(User.vk_id == 44633124).limit(1)
        return [j.id for j in vk_id_query][0]        
    else:
        return False

# проверяем наличие юзера в базе
def check_half(user_id):
    print('user_id =', user_id)
    vk_id_query = session.query(DatingUser)
    vk_id_list = [i.vk_id for i in vk_id_query]
    if user_id in vk_id_list:
        return True        
    else:
        return False

