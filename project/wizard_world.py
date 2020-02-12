from .wizard_structures import *

def get_note_list(username):
	u = Wizard.query.filter_by(username=username).first()
	return u.notes if u	else False

def authenticate(username, password):
    u = Wizard.query.filter_by(username=username).first()
    return u and u.password == password

def register(username, password, email):
    if not Wizard.query.filter_by(username=username).first():
        u = Wizard(username=username, email=email, password=password)
        db.session.add(u)
        db.session.commit()
        return True
    else:
        return False