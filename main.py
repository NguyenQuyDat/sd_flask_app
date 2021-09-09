import threading

from flask import Flask

import config
from app.api import debug
import utils


app = Flask(__name__, static_url_path="", static_folder="./template", template_folder="./template")
app.register_blueprint(debug.api, url_prefix='/')


if __name__ == '__main__':
    thread = threading.Thread(target=utils.save_image_from_camera)
    thread.start()
    app.run(host=config.Config.HOST, port=config.Config.PORT, threaded=True, use_reloader=True, debug=True)
