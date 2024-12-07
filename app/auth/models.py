from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(UserMixin, db.Model):
    """
    User model for authentication.
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    password_hash: Mapped[str | None] = mapped_column(String(256))

    def __repr__(self):
        return f'<User {self.id}>'

    def set_password(self, password) -> None:
        """
        Sets a hashed password for the user.

        :param password: Plain text password to hash and store.
        :return: None
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        """
        Checks if the provided password matches the stored hash.

        :param password: Plain text password to validate.
        :return: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create(email: str, password: str) -> "User":
        """
        Creates a new user with a hashed password and saves it to the database.

        :param email: User's email address.
        :param password: Plain text password to hash.
        :return: User instance.
        """
        user = User(email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def get_by_email(email: str) -> "User | None":
        """
        Retrieves a user by email.

        :param email: User's email address.
        :return: User instance if found, None otherwise.
        """
        return db.session.query(User).filter_by(email=email).first()
