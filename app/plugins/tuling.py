import requests,json

class Tuling:
    def __init__(self,apikey,msg):
        self.url = "http://openapi.tuling123.com/openapi/api/v2"
        self.headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        self.payload = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": msg
                }
            },
            "userInfo": {
                "apiKey": apikey,
                "userId": "1"
            }
        }
    def create_reply(self):
        response = requests.post(self.url,data=json.dumps(self.payload,ensure_ascii=False).encode('utf-8'),headers=self.headers)
        try:
            return response.json().get('results')[0].get('values').get('text')
        except Exception as e:
            return response.text