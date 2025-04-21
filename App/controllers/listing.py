from App.models import listing
from App.models import db

def create_listing(description, price, bedrooms, bathrooms):
    newlisting=listing(description=description, price=price, bedrooms=bedrooms, bathrooms=bathrooms)
    db.session.add(newlisting)
    db.session.commit()
    return newlisting