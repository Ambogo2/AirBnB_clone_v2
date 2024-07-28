#!/usr/bin/python3
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/states', strict_slashes=False)
def states():
    """Display all states sorted by name (A->Z)."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    
    return render_template('states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Display a state and its cities by id."""
    state = storage.get(State, id)
    
    if not state:
        return "<h1>Not found!</h1>", 404

    cities = sorted(state.cities, key=lambda c: c.name) if hasattr(state, 'cities') else []
    
    return render_template('state_by_id.html', state=state, cities=cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
