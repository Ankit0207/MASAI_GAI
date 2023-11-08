from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


@app.route('/weather/<string:city>')
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city]), 200
    else:
        return jsonify({'error': 'City not found'}), 404


# Add new weather data for a city
@app.route('/weather/', methods=['POST'])
def add_weather():
    data = request.get_json()
    city = data.get('city')
    temperature = data.get('temperature')
    weather = data.get('weather')

    if city and temperature is not None and weather:
        weather_data[city] = {'temperature': temperature, 'weather': weather}
        return jsonify({'message': f'Weather data for {city} added'}), 200
    else:
        return jsonify({'error': 'Invalid data provided'}), 400


# Update the weather data for a city
@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    data = request.get_json()

    if city in weather_data:
        if 'temperature' in data:
            weather_data[city]['temperature'] = data['temperature']
        if 'weather' in data:
            weather_data[city]['weather'] = data['weather']
        return jsonify({'message': f'Weather data for {city} updated'}), 200
    else:
        return jsonify({'error': 'City not found'}), 404


# Delete the weather data for a city
@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return jsonify({'message': f'Weather data for {city} deleted'}), 200
    else:
        return jsonify({'error': 'City not found'}), 404


if __name__ == '__main__':
    app.run()
