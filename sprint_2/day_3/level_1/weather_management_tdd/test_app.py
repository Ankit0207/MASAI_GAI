import json
from app import app,weather_data


def test_get_weather_valid_city():
    client = app.test_client()
    response = client.get('/weather/San Francisco')
    print(response)
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'temperature': 14, 'weather': 'Cloudy'}


def test_get_weather_invalid_city():
    client = app.test_client()
    response = client.get('/weather/Unknown City')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 404
    assert data == {'error': 'City not found'}


def test_add_weather_valid():
    client = app.test_client()
    new_data = {'city': 'Chicago', 'temperature': 15, 'weather': 'Cloudy'}
    response = client.post('/weather/', json=new_data)
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'message': 'Weather data for Chicago added'}
    # Check if the data was actually added to the weather_data dictionary
    assert 'Chicago' in weather_data
    assert weather_data['Chicago'] == {'temperature': 15, 'weather': 'Cloudy'}


def test_add_weather_invalid_missing_data():
    client = app.test_client()
    new_data = {'city': 'Houston'}  # Missing temperature and weather
    response = client.post('/weather/', json=new_data)
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert data == {'error': 'Invalid data provided'}
    # Check that no data was added to the weather_data dictionary
    assert 'Houston' not in weather_data


def test_update_weather_valid():
    client = app.test_client()
    updated_data = {'temperature': 18, 'weather': 'Sunny'}
    response = client.put('/weather/New York', json=updated_data)
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'message': 'Weather data for New York updated'}
    # Check if the data was actually updated in the weather_data dictionary
    assert weather_data['New York'] == {'temperature': 18, 'weather': 'Sunny'}


def test_update_weather_invalid_city_not_found():
    client = app.test_client()
    updated_data = {'temperature': 18, 'weather': 'Sunny'}
    response = client.put('/weather/Unknown City', json=updated_data)
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 404
    assert data == {'error': 'City not found'}
    


def test_delete_weather_valid():
    client = app.test_client()
    response = client.delete('/weather/Los Angeles')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'message': 'Weather data for Los Angeles deleted'}
    # Check that data for 'Los Angeles' was actually deleted from the weather_data dictionary
    assert 'Los Angeles' not in weather_data


def test_delete_weather_invalid_city_not_found():
    client = app.test_client()
    response = client.delete('/weather/Unknown City')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 404
    assert data == {'error': 'City not found'}
    # Check that data in the weather_data dictionary remains unchanged
    assert 'Unknown City' not in weather_data
