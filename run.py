from models.base import db
from app import create_app
__author__ = 'anRan'


app = create_app()

db.create_all(app=app)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], threaded=True)
