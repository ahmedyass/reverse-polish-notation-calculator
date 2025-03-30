import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.crud import create_calculation, get_all_calculations
from app.models import Calculation

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

def test_create_calculation(db):
    calc = create_calculation(db, "3 5 +")
    assert calc.expression == "3 5 +"
    assert calc.result == 8

def test_get_all_calculations(db):
    initial_count = len(get_all_calculations(db))

    create_calculation(db, "2 3 *")
    create_calculation(db, "10 5 -")

    calculations = get_all_calculations(db)
    
    assert len(calculations) == initial_count + 2

