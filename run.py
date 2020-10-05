import os
from app import create_app, config_by_name

app = create_app(os.getenv('FLASK_CONFIG'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)