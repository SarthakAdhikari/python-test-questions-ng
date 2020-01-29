from flask import current_app as app

from .load_data import load_data

@app.cli.command("populatedb")
def populate_table():
    load_data()
