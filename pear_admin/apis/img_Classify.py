from flask import Blueprint, request,jsonify,current_app,send_file
from flask_sqlalchemy.pagination import Pagination
import os,time

from aip import AipImageClassify
APP_ID = '66882825'
API_KEY = 'eLqKCZUg0786XOfy7yVjARsE'
SECRET_KEY = 'LS3qlwUQPX28SXQ8ObsMMCOoE3uLrHPf'
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

from pear_admin.extensions import db

img_Classify_api = Blueprint("img_Classify", __name__)


""" 存储POST图片 """
def save_file(file):
    current_app.config['imagepath']=os.path.join(os.getcwd(),'static','images')
    if not os.path.exists(current_app.config['imagepath']):
       os.mkdir(current_app.config['imagepath'])

    filename = str(time.time())+'.png'
    file.get('file').save(os.path.join(current_app.config['imagepath'],filename))
    
    return filename


""" 读取文件 """
def get_file_content(filePath):
  with open(filePath, "rb") as fp:
     return fp.read()


""" 1. 调用车型检测识别 """
def car_Detect(filePath):
  image = get_file_content(filePath)
  res_data = client.carDetect(image)['result']
#   print(res_data)
  return res_data


@img_Classify_api.get('/getfile')
def getfile():
    filename=request.args.get('filename')
    if filename is None:
        return jsonify(code=400,message='参数错误')
    if len(filename.split('.png'))==0 :
        return jsonify(code=400,messages='格式错误')
    try:
        file=send_file(os.path.join( current_app.config['imagepath'],filename),mimetype='image/png')
    except Exception:
        return jsonify(code=400,messages='文件不存在')
    return file
    


@img_Classify_api.post("/img_Classify/carDetect")
def run_img_Classify():
    file = request.files
    if file.get('file') is None:
        return jsonify(code=400,messages='参数不存在')
    
    filename = save_file(file)
    url='/api/v1/getfile?filename='+filename
    
    filepath = 'static/images/' + filename
    res_dict = car_Detect(filepath)

    return {"code": 0, "data": res_dict, "url": url}


