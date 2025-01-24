from flask import Flask

app=Flask(__name__)

from blogcompany.core.views import core
app.register_blueprint(core)