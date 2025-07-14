import asyncio
import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_create_order_and_background_task(capfd):
    response = client.post("/orders/", json={
        "product_name": "Gadget",
        "quantity": 3,
        "customer_email": "customer@test.com"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["product_name"] == "Gadget"
    assert data["status"] == "pending"
    order_id = data["id"]
    # Wait a moment for background task to execute
    asyncio.run(asyncio.sleep(0.2))
    captured = capfd.readouterr().out
    assert f"[MOCK EMAIL] Sent confirmation for order {order_id} to customer@test.com" in captured
