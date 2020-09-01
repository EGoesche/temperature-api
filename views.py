from flask import Blueprint, jsonify, request
from app import db
from models import Temperature

main = Blueprint('main', __name__)

# Route to answer for standard request
@main.route('/')
def welcome():
    return 'Welcome to the Temperature-API!'

# Route to get all temperatures
@main.route('/temperatures')
def list_temperature():
    temperature_list = Temperature.query.all()
    temperatures = []

    for temperature in temperature_list:
        temperatures.append({'id' : temperature.id, 'date' : temperature.date, 'degrees' : temperature.degrees})

    return jsonify({'temperatures' : temperatures}), 200

# Route to add a temperature
@main.route('/temperatures', methods=['POST'])
def add_temperature():
    temperature_data = request.get_json()
    
    new_temperature = Temperature(date=temperature_data['date'], degrees=temperature_data["degrees"])
    db.session.add(new_temperature)
    db.session.commit()

    return 'Temperature was added successfully.', 201

# Route to delete a temperature
@main.route('/temperatures', methods=['DELETE'])
def delete_temperature():
    temperature_data = request.get_json()
    
    Temperature.query.filter_by(id=temperature_data['id']).delete()
    db.session.commit()

    return 'Temperature with id ' + str(temperature_data['id']) + ' was deleted successfully.', 200

# Route to update a existing temperature
@main.route('/temperatures', methods=['PUT'])
def update_temperature():
    temperature_data = request.get_json()
    
    temperature = Temperature.query.get(temperature_data['id'])
    temperature.date = temperature_data['date']
    temperature.degrees = temperature_data['degrees']
    db.session.commit()

    return 'Temperature with id ' + str(temperature_data['id']) + ' was updated successfully.', 200