import threading
from flask import Flask
import os
import sys
import logging

app = Flask("keepalive")

@app.route('/', methods=['GET', 'POST', 'CONNECT', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'TRACE', 'HEAD'])
def main():
    repl_owner = os.environ.get('REPL_OWNER')
    return f'''Hey there, {repl_owner}! I'm Online!'''

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.disabled = True
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

def run_flask_app():
    app.run(host='0.0.0.0',port=7084, debug=False, use_reloader=False)

Welcomer = """\033[1;31m⚠️ Look on Rebot to keep_alive!\033[0m
\033[1;33mPlease note that the .env file cannot exist on (Replit).
Instead, create environment variable DISCORD_TOKEN in the "Secrets".\033[0m
"""

def run_flask_in_thread():
    threading.Thread(target=run_flask_app).start()
    print(Welcomer)
    repl_owner_name = os.environ.get('REPL_OWNER')
    repl_project_name = os.environ.get('REPL_SLUG')
    print(f"\033[1;34m\n\n Hier is link to Rebot URL:\033[0m \n\n https://{repl_project_name}.{repl_owner_name}.repl.co\n\n")

if __name__ == "__main__":
    run_flask_in_thread()