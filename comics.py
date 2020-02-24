import requests
import urllib.request
from twilio.rest import Client
import os

def send_text(current_num,title, secret_text,image_url):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body = f"XKCD Comic {current_num}: {title} \nAlt Text: {secret_text}",
            media_url=[image_url],
            from_= os.environ['TWILIO_PHONE_NUMBER'],
            to = os.environ['TO_PHONE_NUMBER']
        )


    try:
        print(message.sid)
        print(message.status)
        
    except:
        print("ERROR: MESSAGE FAILED TO SEND")

# IF SUCCESSFUL, update number

url = "https://xkcd.com/info.0.json"

r = requests.get(url)

data = r.json()

title = data['safe_title']
image_url = data['img']
secret_text = data['alt']
current_num = data['num']
perm_url = f"https://xkcd.com/{current_num}"

#opens the file and checks what the number is then compares it to the most current number
last_sent_num = [line.strip() for line in open("num.txt")][0]

if (int(current_num) != int(last_sent_num)):
    #XKCD has been updated, go ahead and send it
    send_text(current_num,title,secret_text,image_url)
    # with open("num.txt", "w") as f:
    #     f.write(str(current_num))
    # assert int(data['num']) == int([line.strip() for line in open("num.txt")][0]), f"ERROR: num.txt didn't update how it was supposed to \
    #     num.txt = {[line.strip() for line in open('num.txt')][0]} And\
    #     data['num'] = {data['num']} "


else:
    #No new comic yet, don't continue
    exit()
