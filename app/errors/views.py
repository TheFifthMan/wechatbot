from . import error_bp

# 在这里自定义错误页面
@error_bp.app_errorhandler(400)
def not_found():
    return "404 Not Found", 400