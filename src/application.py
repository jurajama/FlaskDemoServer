from flask import Flask
from api import api_bp

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    # You can access configuration like app.config['FOO'])

    app.register_blueprint(api_bp, url_prefix='/api')

    return app
	
if __name__ == "__main__":
    # "config" refers to config.py
    app = create_app("config")
    app.run(host='0.0.0.0', port=5090, debug=True)