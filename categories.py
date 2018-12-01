from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

cat1 = Category(name="Soccer")

session.add(cat1)
session.commit()

item1 = Item(user_id=1, name="Two shinguards", category=cat1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Shinguards", category=cat1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Jersey", category=cat1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Soccer Cleats", category=cat1)

session.add(item4)
session.commit()


cat2 = Category(name="Basketball")

session.add(cat2)
session.commit()


cat3 = Category(name="Baseball")

session.add(cat3)
session.commit()

item5 = Item(user_id=1, name="Bat", category=cat3)

session.add(item5)
session.commit()

cat4 = Category(name="Frisbee")

session.add(cat4)
session.commit()

item6 = Item(user_id=1, name="Frisbee", category=cat4)

session.add(item6)
session.commit()

cat5 = Category(name="Snowboarding")

session.add(cat5)
session.commit()

item7 = Item(user_id=1, name="Snowboard", category=cat5)

session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Goggles", category=cat5)

session.add(item8)
session.commit()

cat6 = Category(name="Rock Climbing")

session.add(cat6)
session.commit()

cat7 = Category(name="Foosball")

session.add(cat7)
session.commit()

cat8 = Category(name="Skating")

session.add(cat8)
session.commit()

cat9 = Category(name="Hockey")

session.add(cat9)
session.commit()

item9 = Item(user_id=1, name="Stick", category=cat9)

session.add(item9)
session.commit()
