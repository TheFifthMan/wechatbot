import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# 在这里设置你的变量
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "mysql+pymysql://root:qwe123@127.0.0.1/wechatbot"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('TOKEN')
    ADMINS = [os.environ.get('ADMIN_LIST')]
    PAGINATE_PER_PAGE = 5
    WECHAT_TOKEN = os.environ.get('WECHAT_TOKEN')
    WECHAT_AES_KEY = os.environ.get('AES_KEY')
    APPID = os.getenv('APPID')
    TULING_APIKEY=os.getenv('TULING_APIKEY')
    ACCESS_URL = os.getenv("ACCESS_URL")
    

Configuration = {
    'dev':Config,
    'default':Config
}