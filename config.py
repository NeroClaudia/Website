import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nero-claudia-secret-123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/db_inventory'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')