from sqlalchemy     import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime, func
from sqlalchemy     import create_engine
from sqlalchemy.ext.declarative     import declarative_base
from sqlalchemy.orm     import sessionmaker

from configs import Configs

engine = create_engine(
    Configs.DATABASE_URL,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class BaseMixin:
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
#     updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())


# class UserSNS(BaseMixin, Base):
#     __tablename__ = 'users_with_sns'
#     email = Column(String(length=255), nullable=True, unique=True)
#     password = Column(String(length=255), nullable=False)
#     status = Column(Enum("active", "deleted", "blocked"), default="active")
#     name = Column(String(length=255), nullable=True)
#     phone_number = Column(String(length=20), nullable=True, unique=True)
#     profile_img = Column(String(length=1000), nullable=True)
#     sns_type = Column(Enum("FB", "GG", "KK"), nullable=True)
#     marketing_agree = Column(Boolean, nullable=True, default=True)
#     # keys = relationship("ApiKeys", back_populates="users")