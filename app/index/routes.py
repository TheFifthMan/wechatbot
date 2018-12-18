from . import index_bp
from .views import Index,WeChat
index_bp.add_url_rule('/',view_func=Index.as_view('index'))
index_bp.add_url_rule('/wechat',view_func=WeChat.as_view('wechat'))


# url_for 的时候怎么用？
# url_for('index.index') index 可以类比为就是这个函数的名字