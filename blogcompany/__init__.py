from flask import Flask

app=Flask(__name__)

from blogcompany.core.views import core
from blogcompany.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)