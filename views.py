from flask import Blueprint, jsonify, request
from app import db
from models import Temperature

main = Blueprint('main', __name__)

@main.route('/temperatures', methods=['POST'])
def add_temperature():
    temperature_data = request.get_json()
    
    new_temperature = Temperature(date=temperature_data['date'], degrees=temperature_data["degrees"])
    db.session.add(new_temperature)
    db.session.commit()

    return 'Done', 201

@main.route('/temperatures')
def list_temperature():
    temperature_list = Temperature.query.all()
    temperatures = []

    for temperature in temperature_list:
        temperatures.append({'date' : temperature.date, 'degrees' : temperature.degrees})

    return jsonify({'temperatures' : temperatures})