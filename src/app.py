"""This module contains REST interface logic"""
from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv

from event_handler import EventHandler

load_dotenv('.env')

event_handler = EventHandler()

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(status=404, error=str(e)), 404


@app.route('/api/v1/resources/accounts/<string:iban>', methods=['GET', 'POST', 'DELETE'])
def account(iban):
    if request.method == 'POST':
        form = request.get_json(force=True)
        if event_handler.upsert_account(form):
            return jsonify(status=201, result=f"IBAN: {form['iban']} upserted.")
        else:
            return jsonify(status=500, error='Server Error')

    if request.method == 'DELETE':
        form = request.get_json(force=True)
        if event_handler.delete_account(form):
            return jsonify(status=200, result=f"IBAN: {form['iban']} deleted.")
        else:
            return jsonify(status=500, error='Server Error')

    if iban == 'all':
        load = event_handler.get_accounts()
    else:
        load = event_handler.get_account(iban)

    if load is not None:
        return jsonify(status=200, result=load)
    else:
        abort(404, description="Resource not found")


@app.route('/api/v1/health')
def health():
    load = event_handler.get_health()
    return jsonify(status=200, result=load)


app.run(host='0.0.0.0')
