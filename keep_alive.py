import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/', methods=['GET', 'POST', 'CONNECT', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'TRACE', 'HEAD'])
def main():
    repl_owner = os.getenv('REPL_OWNER')
    return f'''Hey there, {repl_owner}! I'm Online!'''

def run():
  app.run(host='0.0.0.0',port=7084)

def keep_alive():
    t = Thread(target=run)
    t.start()