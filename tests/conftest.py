import pytest
from app.db.session import engine, Base
import app.models.user
import app.models.task

@pytest.fixture(scope="session", autouse=True)
def create_test_tables():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)