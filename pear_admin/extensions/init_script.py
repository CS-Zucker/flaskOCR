import csv
import os

from flask import Flask, current_app

from pear_admin.extensions import db
from pear_admin.orms import RightsORM, RoleORM, UserORM


def register_script(app: Flask):
    @app.cli.command()
    def init():
        db.drop_all()
        db.create_all()

        root = current_app.config.get("ROOT_PATH")
        sql_data_path = os.path.join(root, "static", "sql", "sql_init.txt")
        # 读取 SQL 文件
        with open(sql_data_path, encoding="utf-8") as f:
            sql_statements = f.read()

        # 使用分号分隔 SQL 语句
        statements = sql_statements.split(';')

        # 执行每个 SQL 语句
        for statement in statements:
            if statement.strip():  # 跳过空语句
                db.session.execute(statement)

        # 提交事务并关闭连接
        db.session.commit()
        