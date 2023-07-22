from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('ejGA5/d+pTJiH9u81CuG/vteoL1BNGdWSNqk6X5do/josbInQ2iBMXe4DH6+f/oExhJG/d1bAOTHFUnkRnqbSi25ie85IVFaUm1s2jbUZRRa6IUI0KwajaBBwKJsZ3/e34kPjCiTeya578z5Kzf1wwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('f96cd94522136ce52084397a48214ad5')

line_bot_api.push_message('Ue436909c33a5e2e1675e24f5a64211aa', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    line_bot_api.reply_message(event.reply_token,TextSendMessage(message))


#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)