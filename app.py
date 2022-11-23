from flask import Flask
from routes import main
# from db import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/ds4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db.init_app(app)
app.register_blueprint(main)

if __name__ == "__main__": 
  app.run(debug=True)