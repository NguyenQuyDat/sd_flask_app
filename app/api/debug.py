import base64

from flask import Blueprint, render_template

import utils
import config


api = Blueprint('debug', __name__)


@api.route('/log', methods=['GET'])
def get_debug_log():
    log_text = utils.get_log()
    return render_template('log.html', log=log_text)


@api.route('/image', methods=['GET'])
def get_debug_image():
    image_path = config.Config.IMAGE_FILE_PATH
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return render_template('image.html', img_data=encoded_string)
