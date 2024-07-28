#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display all states and their cities"""
    states = storage.all(State)
    
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    
    states_data = []
    for state in sorted_states:
        state_cities = sorted(state.cities, key=lambda c: c.name) if hasattr(state, 'cities') else []
        state_info = {
            'id': state.id,
            'name': state.name,
            'cities': [{'id': city.id, 'name': city.name} for city in state_cities]
        }
        states_data.append(state_info)
    
    return render_template('cities_by_states.html', states=states_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
