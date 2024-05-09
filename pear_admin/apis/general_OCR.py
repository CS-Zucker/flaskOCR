from flask import Blueprint, request,jsonify,current_app,send_file
from flask_sqlalchemy.pagination import Pagination
import os,time

from aip import AipOcr
APP_ID = '59228085'
API_KEY = 'BTrWaPF1h5x9ONDidTWaHfTa'
SECRET_KEY = '5zlJfbk7aYiwwc9ILm0Yl4hEV5mc0MwH'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

from pear_admin.extensions import db

general_OCR_api = Blueprint("general_OCR", __name__)


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


""" 1. 调用OCR文字识别 """
def general_OCR(filePath):
  image = get_file_content(filePath)
  res_data = client.basicAccurate(image)
  reslist = []
  for item in res_data['words_result']:
    reslist.append(item['words'])
  return reslist

""" 2. 调用OCR印章识别 """
def seal_OCR(filePath):
  image = get_file_content(filePath)
  res_data = client.seal(image)
  reslist = []
  for i, item in enumerate(res_data['result']):
    reslist.append("结果" + str(i+1) + ":")
    reslist.append(f"宽度： {item['location']['width']}")
    reslist.append(f"高度： {item['location']['height']}")
    reslist.append(f"上边距： {item['location']['top']}")
    reslist.append(f"左边距： {item['location']['left']}")
    reslist.append(f"上环主要文字： {item['major']['words']}")
    for j, minor_item in enumerate(item['minor']):
        reslist.append(f"其他位置文字{j+1}： {minor_item['words']}")
    reslist.append(' ')
  return reslist

@general_OCR_api.get('/getfile')
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


@general_OCR_api.post("/general_OCR/word")
def run_general_OCR():
    file = request.files
    if file.get('file') is None:
        return jsonify(code=400,messages='参数不存在')
    
    filename = save_file(file)
    url='/api/v1/getfile?filename='+filename
    
    filepath = 'static/images/' + filename
    res_list = general_OCR(filepath)
    res_str = '\n'.join(res_list)
      
    return {"code": 0, "data": res_str, "url": url}


@general_OCR_api.post("/general_OCR/seal")
def run_seal_OCR():
    file = request.files
    if file.get('file') is None:
        return jsonify(code=400,messages='参数不存在')
    
    filename = save_file(file)
    url='/api/v1/getfile?filename='+filename
    
    filepath = 'static/images/' + filename
    res_list = seal_OCR(filepath)
    res_str = '\n'.join(res_list)
      
    return {"code": 0, "data": res_str, "url": url}

