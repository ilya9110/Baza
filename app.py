from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rashodniki.db'

db = SQLAlchemy(app)

class Rashodniki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ostatok = db.Column(db.String(50))

    def __init__(self, name, ostatok):
        self.name = name
        self.ostatok = ostatok


with app.app_context():
    db.create_all()

@app.route('/add_rashodniki', methods=['POST'])
def add_employee():
    name = request.form['name']
    ostatok = request.form['ostatok']
    rashodniki = Rashodniki(name, ostatok)
    db.session.add(rashodniki)
    db.session.commit()
    return {"success": 'Rashodniki added successfully'}

@app.route('/get_rashodniki/<int:id>')
def get_rashodniki(id):
    rashodniki = Rashodniki.query.get(id)
    if rashodniki:
        return jsonify({
            'id': rashodniki.id,
            'name': rashodniki.name,
            'ostatok': rashodniki.ostatok
        })
    else:
        return {'error': 'Rashodniki not found'}




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)