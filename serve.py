from api import wsgi
import bjoern


bjoern.run(wsgi.application, 'localhost', 8080)
