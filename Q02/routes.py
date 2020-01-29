from flask import render_template
from flask import current_app as app

@app.route('/')
def view_userLst():
    return render_template('datatable_example.html', api='/api/users')