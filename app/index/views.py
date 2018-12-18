from flask.views import MethodView
from flask import request,current_app,abort
from app.plugins.tuling import Tuling
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import (
    InvalidSignatureException,
    InvalidAppIdException,
)

class Index(MethodView):
    def __init__(self,*args,**kw):
        self.message ="Server Up message"
        super(Index,self).__init__(*args,**kw)

    def get(self):
        return self.message

class WeChat(MethodView):
    def __init__(self,*args,**kw):
        self.signature = request.args.get('signature')
        self.timestamp = request.args.get('timestamp')
        self.nonce = request.args.get('nonce')
        self.encrypt_type = request.args.get('encrypt_type', 'raw')
        self.msg_signature = request.args.get('msg_signature', '')
        self.TOKEN = current_app.config['WECHAT_TOKEN']
        self.AES_KEY = current_app.config['WECHAT_AES_KEY']
        self.APPID = current_app.config['APPID']
        super(WeChat,self).__init__(*args,**kw)


    def get(self):
        try:
            check_signature(self.TOKEN, self.signature, self.timestamp, self.nonce)
        except InvalidSignatureException:
            abort(403)
        
        echo_str = request.args.get('echostr', '')
        return echo_str

    def post(self):

        # if self.encrypt_type == 'raw':
        #     # plaintext mode
        #     msg = parse_message(request.data)
        #     if msg.type == 'text':
        #         reply = create_reply(msg.content, msg)
        #     else:
        #         reply = create_reply('Sorry, can not handle this for now', msg)
        #     return reply.render()
        # else:
        # encryption mode
        from wechatpy.crypto import WeChatCrypto

        crypto = WeChatCrypto(self.TOKEN, self.AES_KEY, self.APPID)
        try:
            msg = crypto.decrypt_message(
                request.data,
                self.msg_signature,
                self.timestamp,
                self.nonce
            )
        except (InvalidSignatureException, InvalidAppIdException):
            abort(403)
        else:
            msg = parse_message(msg)
            if msg.content == "help":
                message = "help \t 帮助信息\t\n " \
                + "hit \t  一言\t\n " \
                + "bing \t 每日壁纸\t\n " \
                + "? \t 有道翻译\t\n "
                reply = create_reply(message,msg)

            elif msg.type == 'text':
                message = Tuling(current_app.config['TULING_APIKEY'],msg.content).create_reply()
                reply = create_reply(message, msg)
            else:
                reply = create_reply('Sorry, can not handle this for now', msg)
            return crypto.encrypt_message(reply.render(), self.nonce, self.timestamp)

