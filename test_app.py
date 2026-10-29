import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_hello_default():
    tester = app.test_client()
    response = tester.get('/hello')

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Hello, World!"
    }


def test_hello_name():
    tester = app.test_client()
    response = tester.get('/hello?name=Michael')

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Hello, Michael!"
    }


def test_sum_success():
    tester = app.test_client()
    response = tester.post('/sum', json={
        "numbers": [1, 2, 3]
    })

    assert response.status_code == 200
    assert response.get_json() == {
        "sum": 6
    }


def test_sum_missing_numbers():
    tester = app.test_client()
    response = tester.post('/sum', json={})

    assert response.status_code == 400


def test_sum_invalid_data():
    tester = app.test_client()
    response = tester.post('/sum', json={
        "numbers": "not_a_list"
    })

    assert response.status_code == 400