from operator import or_
from sqlmodel import Session, select, func

from models.user import User

class UserQuery:
    def __init__(self, session: Session):
        self.db = session

    def is_substring(self):

        query = select(User)

        return self.db.exec(query).all()