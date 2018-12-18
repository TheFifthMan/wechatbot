from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import logging
from logging.handlers import SMTPHandler,RotatingFileHandler
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Configuration[config_name])
    db.init_app(app)
    migrate.init_app(app,db)
   
    # 在这里注册蓝图
    from app.errors import error_bp
    app.register_blueprint(error_bp)
    from app.index import index_bp
    app.register_blueprint(index_bp)
    
    # 相关的东西需要引入进来，实际就是一个单文件
    if not app.debug:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_SSL']:
                secure = ()

            mail_handler = SMTPHandler(
                mailhost=app.config['MAIL_SERVER'],
                fromaddr=app.config['MAIL_USERNAME'],
                toaddrs=app.config['ADMINS'],
                subject="Microblog Error",
                credentials=auth,secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

            if not os.path.exists('logs'):
                os.mkdir('logs')
            
            file_handler = RotatingFileHandler('logs/microblog.log',maxBytes=10240,backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.info('app start.')
        
    
    return app