from flask import Flask, Response, render_template, jsonify, request, abort,\
                  Blueprint, g
from .validation import JsonValidation, ArgsValidation
from .report import LogReport
from pymongo import errors
import requests
import logging
import json
import sys
import datetime
import os
import ast
from bson.objectid import ObjectId

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def index():
    return 'dash_api has been started'

@api.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip', type=str)
    response = os.system("ping -c 1 " + ip)
    if(response == 0):
        return 'On'
    else:
        return 'Fail'

@api.route('/group', methods=['GET'])
def get_group():
    response = list(g.db.group_collection.find({}))
    for document in response:
        document['_id'] = str(document['_id'])

    return jsonify(response), 200

@api.route('/group', methods=['POST'])
def group_register():
    group = request.get_json() if request.is_json else request.form.to_dict()
    print(group)
    if not JsonValidation().group_validation(group):
        abort(400)
    try:
        g.db.group_collection.update_one(group, {'$set': group},
                                          upsert=True)
    except errors.WriteError:
        return jsonify({'code': 500, 'message': 'Internal Server Error'}), 500
    return jsonify({'code': 200, 'message': 'Success'}), 200

@api.route('/group/<group_id>', methods=['DELETE'])
def delete_group(group_id):
    id = group_id
    try:
        g.db.group_collection.remove({ '_id': ObjectId(id) })
    except errors.WriteError:
        return jsonify({'code': 500, 'message': 'Internal Server Error'}), 500
    return jsonify({'code': 200, 'message': 'Success'}), 200

@api.route('/group/client/<group_id>', methods=['POST'])
def client_register(group_id):
    id = group_id
    client = request.get_json() if request.is_json else request.form.to_dict()
    if not JsonValidation().client_validation(client):
        abort(400)
    identifier = {}
    identifier['mac'], identifier['chipset'] = client['mac'], client['chipset']
    response = requests.get('https://uiot-dims.herokuapp.com/list/service', params=identifier)
    result = ast.literal_eval(response.text)
    for document in result:
        document['groupId'] = id
        document['commands'] = []
    try:
        g.db.group_collection.update({ '_id': ObjectId(id) }, { '$push': { "clients": client } })
        g.db.service_collection.insert(result)
    except errors.WriteError:
        return jsonify({'code': 500, 'message': 'Internal Server Error'}), 500
    return jsonify({'code': 200, 'message': 'Success'}), 200

@api.route('/group/client/delete/<group_id>', methods=['POST'])
def client_delete(group_id):
    id = group_id
    client = request.get_json() if request.is_json else request.form.to_dict()
    print(client)
    if not JsonValidation().client_validation(client):
        abort(400)
    try:
        g.db.group_collection.update({ '_id': ObjectId(id) }, { '$pull': { "clients": client } })
        g.db.service_collection.remove({ 'groupId': id })
    except errors.WriteError:
        return jsonify({'code': 500, 'message': 'Internal Server Error'}), 500
    return jsonify({'code': 200, 'message': 'Success'}), 200

@api.route('/service', methods=['GET'])
def get_service():
    response = list(g.db.service_collection.find({}))
    for document in response:
        document['_id'] = str(document['_id'])
    return jsonify(response), 200

@api.route('/service/<mac>/<chipset>')
def get_by_client(mac, chipset):
    response = list(g.db.service_collection.find({ 'mac': mac, 'chipset': chipset }))
    for document in response:
        document['_id'] = str(document['_id'])

    return jsonify(response), 200

@api.route('/service/command/<service_id>')
def add_command(service_id):
    id = service_id
    command = request.get_json() if request.is_json else request.form.to_dict()


@api.route('/delete/all', methods=['GET'])
def delete_all():
    try:
        g.db.service_collection.remove({})
    except errors.WriteError:
        return jsonify({'code': 500, 'message': 'Internal Server Error'}), 500
    return jsonify({'code': 200, 'message': 'Success'}), 200
