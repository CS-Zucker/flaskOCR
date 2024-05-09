from collections import OrderedDict
from copy import deepcopy

from flask import jsonify
from flask import Blueprint, make_response, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_current_user,
    jwt_required,
)

from pear_admin.extensions import db
from pear_admin.orms import RightsORM, RoleORM, UserORM, user_role, role_rights

passport_api = Blueprint("passport", __name__)


@passport_api.post("/login")
def login_in():
    data = request.get_json()

    user: UserORM = db.session.execute(
        db.select(UserORM).where(UserORM.username == data["username"])
    ).scalar()

    if not user:
        return {"message": "用户不存在", "code": -1}, 401
    if user.password != data["password"]:
        return {"message": "用户密码错误", "code": -1}, 401

    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)

    response = make_response(
        {
            "code": 0,
            "msg": "登录成功",
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    )

    return response


@passport_api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    nickname = data.get('nickname')
    mobile = data.get('mobile')
    email = data.get('email')

    if not username or not password or not nickname or not mobile or not email:
        return jsonify({'message': '请填写完整信息'})

    if UserORM.query.filter_by(username=username).first():
        return jsonify({'message': '用户名已存在'})

    new_user = UserORM(
        username=username,
        password=password,
        nickname=nickname,
        mobile=mobile,
        email=email
    )
    db.session.add(new_user)
    db.session.commit()
    
    user_id = new_user.id
    new_user_role = user_role.insert().values(user_id=user_id, role_id=3)
    db.session.execute(new_user_role)
    db.session.commit()

    return jsonify({'message': '注册成功'})

@passport_api.route("/logout", methods=["GET", "POST"])
@jwt_required()
def logout():
    return {"msg": "退出登录成功", "code": 0}


@passport_api.get("/menu")
@jwt_required()
def menus_api():
    rights_orm_list = set()
    current_user: UserORM = get_current_user()
    for role in current_user.role_list:
        for rights_orm in role.rights_list:
            if rights_orm.type != "auth":
                rights_orm_list.add(rights_orm)

    rights_list = [rights_orm.menu_json() for rights_orm in rights_orm_list]
    rights_list.sort(key=lambda x: (x["pid"], x["id"]), reverse=True)

    menu_dict_list = OrderedDict()
    for menu_dict in rights_list:
        if menu_dict["id"] in menu_dict_list.keys():  # 如果当前节点已经存在于字典中
            # 当前节点添加子节点
            menu_dict["children"] = deepcopy(menu_dict_list[menu_dict["id"]])
            menu_dict["children"].sort(key=lambda item: item["sort"])
            # 删除子节点
            del menu_dict_list[menu_dict["id"]]

        if menu_dict["pid"] not in menu_dict_list:
            menu_dict_list[menu_dict["pid"]] = [menu_dict]
        else:
            menu_dict_list[menu_dict["pid"]].append(menu_dict)

    return sorted(menu_dict_list.get(0), key=lambda item: item["sort"])
