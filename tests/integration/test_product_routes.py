import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products/", json={"name": "Tênis", "price": 129.9, "quantity": 5})
    assert response.status_code == 200
    assert response.json()["name"] == "Tênis"