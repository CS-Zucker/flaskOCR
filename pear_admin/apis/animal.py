from datetime import datetime

import requests
import base64
from flask import Blueprint, request, jsonify, current_app, send_file

import os, time
from flask_jwt_extended import current_user, jwt_required
from flask_sqlalchemy.pagination import Pagination

from pear_admin.extensions import db


animal_api = Blueprint("animal", __name__)


def save_file(file):
    current_app.config['imagepath'] = os.path.join(os.getcwd(), 'static', 'images')
    if not os.path.exists(current_app.config['imagepath']):
        os.mkdir(current_app.config['imagepath'])

    filename = str(time.time()) + '.png'
    file.get('file').save(os.path.join(current_app.config['imagepath'], filename))

    return os.path.join(current_app.config['imagepath'], filename)


""" 读取文件 """


def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()


def animal_recognition(filePath):
    image_data = get_file_content(filePath)
    encoded_image = base64.b64encode(image_data).decode('utf-8')

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    access_token = '24.424ab265c84ba0b0f5792037002a4098.2592000.1717576663.282335-67490976'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {"image": encoded_image}
    response = requests.post(request_url, data=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "An error occurred during animal recognition"}


def fruit_rec(filePath):
    image_data = get_file_content(filePath)
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"
    access_token = '24.b3e86842bf6e477c328b526b8ef8893a.2592000.1717556587.282335-67402442'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {"image": encoded_image}
    response = requests.post(request_url, data=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "An error occurred during animal recognition"}


def eat_rec(filePath):
    image_data = get_file_content(filePath)
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
    access_token = '24.424ab265c84ba0b0f5792037002a4098.2592000.1717576663.282335-67490976'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {"image": encoded_image}
    response = requests.post(request_url, data=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "An error occurred during animal recognition"}


@animal_api.get('/getfile')
def getfile():
    filename = request.args.get('filename')
    if filename is None:
        return jsonify(code=400, message='参数错误')
    if len(filename.split('.png')) == 0:
        return jsonify(code=400, messages='格式错误')
    try:
        file = send_file(os.path.join(current_app.config['imagepath'], filename), mimetype='image/png')
    except Exception:
        return jsonify(code=400, messages='文件不存在')
    return file


@animal_api.route('/animal_recognition', methods=['POST'])
def animal_recognition_endpoint():
    file = request.files
    if file.get('file') is None:
        return jsonify(code=400, messages='参数不存在')

    filename = save_file(file)
    url = '/api/v1/getfile?filename=' + filename
    res_dict = animal_recognition(filename)
    return {"code": 0, "data": res_dict['result'], "url": url}


@animal_api.route('/fruit_recognition', methods=['POST'])
def fruit_recognition_endpoint():
    file = request.files
    if file.get('file') is None:
        return jsonify(code=400, messages='参数不存在')

    filename = save_file(file)
    url = '/api/v1/getfile?filename=' + filename
    res_dict = fruit_rec(filename)
    return {"code": 0, "data": res_dict['result'], "url": url}


@animal_api.route('/eat_recognition', methods=['POST'])
def eat_recognition_endpoint():
    file = request.files
    if file.get('file') is None:
        return jsonify(code=400, messages='参数不存在')

    filename = save_file(file)
    url = '/api/v1/getfile?filename=' + filename
    res_dict = eat_rec(filename)
    return {"code": 0, "data": res_dict['result'], "url": url}







