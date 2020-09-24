from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now()
    html1 = str(socket.gethostname())
    html2 = now.strftime("%m/%d/%Y %H:%M:%S")
    html = '<h1 style="color:DodgerBlue;"> Hello Google!' + "</h1></br>" + "Time is: " + html2
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
