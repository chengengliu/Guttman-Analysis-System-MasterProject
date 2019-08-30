from .__init__ import app, db_conn
from .models import auth


@app.route('/auth', methods=['POST'])
def login():
    return auth.login(
        app=app,
        db_conn=db_conn
    )
