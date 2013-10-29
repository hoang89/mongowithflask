import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from withdb import app

manage = Manager(app)

manage.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=80
))

def register_blueprints(app):
    # Prevents circular imports
    from withdb.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
    manage.run()
