from flask import Flask
from app.main import main as main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

app.run(debug=True)
