from .user import create_user
from .landlord import create_landlord
from .tenant import create_tenant
from .Amenities import create_Amenity
from .listing import create_listing
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob','bob@gmail.com','bobpass')
    jill=create_landlord("jill","jill@gmail.com","jillpass")
    print(jill.id)
    print("lolllllllllllllllllllllllllllllll")
    mike=create_tenant("mike","mike@gmail.com","mikepass")
    a1=create_Amenity("Wifi")
    a2=create_Amenity("Air Conditioning")
    a3=create_Amenity("Swimming Pool")
    a4=create_Amenity("Pets Allowed")
    #p1=create_listing("Cozy 2-bedroom apartment with sea view",125.00,2,2)
    db.session.add_all([jill,mike,a1,a2,a3,a4])
    #db.session.add(mike)
    db.session.commit()

