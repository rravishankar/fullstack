# class Venue(db.Model):
#     __tablename__ = 'Venue'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     address = db.Column(db.String(120))
#     phone = db.Column(db.String(120))
#     image_link = db.Column(db.String(500))
#     facebook_link = db.Column(db.String(120))

#     # TODO: implement any missing fields, as a database migration using Flask-Migrate
#     shows = db.relationship("Show", lazy=True, cascade="all, delete-orphan")

# class Artist(db.Model):
#     __tablename__ = 'Artist'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     phone = db.Column(db.String(120))
#     genres = db.Column(db.String(120))
#     image_link = db.Column(db.String(500))
#     facebook_link = db.Column(db.String(120))

#     # TODO: implement any missing fields, as a database migration using Flask-Migrate
#     show_association = db.relationship("Show", lazy=True, cascade="all, delete-orphan")


# # TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

# class Show(db.Model):
#     __tablename__ = 'Show'
#     #Ref https://stackoverflow.com/questions/30406808/flask-sqlalchemy-difference-between-association-model-and-association-table-fo
#     artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=True),
#     venue_id = db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
#     show_time = (db.DateTime, nullable=False, primary_key=True)




