import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_root():
    """ルートエンドポイントのテスト"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Addition API"}


def test_add_positive_numbers():
    """正の数の加算テスト"""
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}


def test_add_negative_numbers():
    """負の数の加算テスト"""
    response = client.post("/add", json={"a": -5, "b": -3})
    assert response.status_code == 200
    assert response.json() == {"result": -8.0}


def test_add_mixed_numbers():
    """正と負の数の加算テスト"""
    response = client.post("/add", json={"a": 10, "b": -7})
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}


def test_add_decimals():
    """小数の加算テスト"""
    response = client.post("/add", json={"a": 1.5, "b": 2.3})
    assert response.status_code == 200
    assert response.json()["result"] == pytest.approx(3.8)


def test_add_zero():
    """ゼロの加算テスト"""
    response = client.post("/add", json={"a": 0, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"result": 0.0}
