from flask import Flask
from app.core import main as main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

app.run(host="127.0.0.1", port="5000", debug=True, use_reloader=True)
