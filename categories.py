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

# user 1
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# category 1
cat1 = Category(name="Soccer")

session.add(cat1)
session.commit()

item1 = Item(user_id=1, name="Shinguards", category=cat1, description = "A piece of equipment worn on the front of a player's shin to protect them from injury")

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Jersey", category=cat1, description = "A knitted garment with long sleeves, worn over the upper body.")

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Soccer Cleats", category=cat1, description = "An item of footwear worn when playing football")

session.add(item3)
session.commit()

################################################################
#category 2

cat2 = Category(name="Basketball")

session.add(cat2)
session.commit()

item4 = Item(user_id=1, name="Shoes", category=cat2, description = "One needs specialized shoes when playing basketball. It should be able to give better support to the ankle as compared to running shoes. The basketball shoes should be high-tipped shoes and provide extra comfort during a game. These shoes are specially designed to maintain high traction on the basketball court.")

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Back Board", category=cat2, description = "The backboard is the rectangular board that is placed behind the rim. It helps give better rebound to the ball. The backboard is about 1800mm in size horizontally and 1050mm vertically. Many times, backboards are made of acrylic, aluminum, steel or glass.")

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Shot Clock", category=cat2, description = "The offense is allowed a maximum of 24 seconds to have a ball in hand before shooting. These 24 seconds are counted on the shot clock. If the offense fails to shoot a ball that hits the rim, they will lose the possession of the ball to the other team.")

session.add(item6)
session.commit()
################################################################
#category 3

cat3 = Category(name="Baseball")

session.add(cat3)
session.commit()

item7 = Item(user_id=1, name="Bat", category=cat3, description = "A rounded, solid wooden or hollow aluminum bat. Wooden bats are traditionally made from ash wood, though maple and bamboo is also sometimes used. Aluminum bats are not permitted in professional leagues, but are frequently used in amateur leagues. Composite bats are also available, essentially wooden bats with a metal rod inside. Bamboo bats are also becoming popular.")

session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Base", category=cat3, description = "One of four corners of the infield which must be touched by a runner in order to score a run; more specifically, they are canvas bags (at first, second, and third base) and a rubber plate (at home).")

session.add(item8)
session.commit()

item9 = Item(user_id=1, name="Catcher's Mitt", category=cat3, description = "Leather mitt worn by catchers. It is much wider than a normal fielder's glove and the four fingers are connected. The mitt is also better-padded than the standard fielder's glove.")

session.add(item9)
session.commit()
################################################################
#category 4

cat4 = Category(name="Frisbee")

session.add(cat4)
session.commit()

item10 = Item(user_id=1, name="Frisbee", category=cat4, description = "It is a gliding toy or sporting item that is generally plastic and roughly 20 to 25 centimetres (8 to 10 in) in diameter with a pronounced lip. It is used recreationally and competitively for throwing and catching")

session.add(item10)
session.commit()


################################################################
#category 5

cat5 = Category(name="Snowboarding")

session.add(cat5)
session.commit()

item11 = Item(user_id=1, name="Snowboard", category=cat5, description = "There are different types of boards (alpine, freestyle, and freeride). Beginners may prefer freestyle boards, as they are shorter and easier to control.")

session.add(item11)
session.commit()

item12 = Item(user_id=1, name="Boots", category=cat5, description = "These specialized boots will connect you to your board through the bindings. Snowboard boots come in regular shoe sizes, but sizing can vary among different companies. Your boots should be snug, but not tight to the point of restriction.")

session.add(item12)
session.commit()

item13 = Item(user_id=1, name="Goggles", category=cat5, description = "Snowboard goggles help battle glare and protect your eyes from the snow and wind while riding. When riding down a mountain, snow and debris can fly against your face, making goggles a necessary piece of equipment.")

session.add(item13)
session.commit()

################################################################
#category 6

cat6 = Category(name="Rock Climbing")

session.add(cat6)
session.commit()

item14 = Item(user_id=1, name="Rope", category=cat6, description = "Climbing ropes are typically of kernmantle construction, consisting of a core (kern) of long twisted fibres and an outer sheath (mantle) of woven coloured fibres")

session.add(item14)
session.commit()

item15 = Item(user_id=1, name="Carabiners", category=cat6, description = "Carabiners are metal loops with spring-loaded gates (openings), used as connectors. Once made primarily from steel, almost all carabiners for recreational climbing are now made from a light weight aluminum alloy")

session.add(item15)
session.commit()

item16 = Item(user_id=1, name="Quickdraws", category=cat6, description = "Quickdraws are used by climbers to connect ropes to bolt anchors, or to other traditional protection, allowing the rope to move through the anchoring system with minimal friction. A quickdraw consists of two non-locking carabiners connected together by a short, pre-sewn loop of webbing")

session.add(item16)
session.commit()
################################################################
#category 7

cat7 = Category(name="Foosball")

session.add(cat7)
session.commit()

item17 = Item(user_id=1, name="Table football", category=cat7, description = "Several companies have created luxury versions of table football tables. There was a 7-metre table created by artist Maurizio Cattelan for a piece called Stadium. It takes 11 players to a side. Differences in the table types have great influence on the playing styles.")

session.add(item17)
session.commit()
################################################################
#category 8

cat8 = Category(name="Skating")

session.add(cat8)
session.commit()

item18 = Item(user_id=1, name="Skates", category=cat8, description = "All figure skaters usually own their own figure skates. Your skates should neatly be packed in your skate bag with soakers protecting the blades.")

session.add(item18)
session.commit()

item19 = Item(user_id=1, name="Gloves", category=cat8, description = "Every figure skater needs gloves during practice. In addition to keeping hands warm, gloves protect a skater's hands if he or she falls on the ice.")

session.add(item19)
session.commit()

item20 = Item(user_id=1, name="Rag", category=cat8, description = "Figure skaters must always dry blades thoroughly after skating. A clean towel or rag should be packed inside a figure skater's skate bag so that a skater can thoroughly wipe blades clean and dry off his or her skating boots.")

session.add(item20)
session.commit()
################################################################
#category 9

cat9 = Category(name="Hockey")

session.add(cat9)
session.commit()

item21 = Item(user_id=1, name="Stick", category=cat9, description = "Made of wood or composite materials, hockey sticks come in various styles and lengths. Stick dimensions vary based on the size of the player. Traditionally, all sticks were wooden up until the late 1990s.")

session.add(item21)
session.commit()

item22 = Item(user_id=1, name="Helmet", category=cat9, description = "A helmet with strap, and optionally a face cage or visor, is required of all ice hockey players. Hockey helmets come in various sizes, and many of the older designs can also be adjusted by loosening or fastening screws at the side or at the back.")

session.add(item22)
session.commit()

item23 = Item(user_id=1, name="Shoulder Pads", category=cat9, description = "Hockey shoulder pads are typically composed of a passed vest with front and back panels, with velcro straps for closure, and soft or hard-shelled shoulder caps with optional attached upper arm pads.")

session.add(item23)
session.commit()
