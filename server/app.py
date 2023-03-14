#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()
    return jsonify([bakery.to_dict() for bakery in bakeries]), 200

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()
    return jsonify(bakery.to_dict()), 200

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    goods = BakedGood.query.order_by(desc(BakedGood.price)).all()
    return jsonify([good.to_dict() for good in goods]), 200

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    good = goods = BakedGood.query.order_by(desc(BakedGood.price)).first()
    return jsonify(good.to_dict()), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
