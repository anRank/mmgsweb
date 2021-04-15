from app.web import web
import base64
from flask import make_response


@web.route("/static/img/<img_file>/")
def get_pic(img_file):
    # # static/img/clannad.jpg
    img_path = "app/static/img/" + img_file
    with open(img_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return img_stream


# @web.route("/static/img/<img_name>/")
# def get_pic(img_name):
#     # # static/img/clannad.jpg
#     img_path = "app/static/img/" + img_name
#     file = open(img_path, 'rb').read()
#     response = make_response(file)
#     utf_filename = quote(img_name.encode("utf-8"))
#     response.headers["Content-Disposition"] = "attachment;filename*=utf-8''{}".format(utf_filename)
#     response.headers["Content-Type"] = "application/octet-stream; charset=UTF-8"
#     return response