from App.models import Amenities
from App.database import db

def create_Amenity(name):
    newamenity= Amenities(name=name)
    db.session.add(newamenity)
    db.session.commit()
    return newamenity