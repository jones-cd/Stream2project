from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'LACdata'
COLLECTION_NAME = 'projects'


@app.route("/")
def index():
    """
    A Flask view to serve the main dashboard page.
    """
    return render_template("index.html")


@app.route("/LACdata/projects")
def LAC_projects():
    """
    A Flask view to serve the project data from
    MongoDB in JSON format.
    """

    # A constant that defines the record fields that we wish to retrieve.
    FIELDS = {
        '_id': False,
        'c': True,    'd1' : True,    'e1' : True,   'f1' : True,   'g1' : True, 'h1' : True, 'j2' : True, 'k2' : True, 'l2' : True,  'm2' : True, 'n2' : True, 'q3': True, 'r3'
        : True, 's3' : True, 't3' : True,  'u3' : True, 'w4' : True, 'x4' : True, 'y4' : True, 'z4' : True, 'aa4' : True, 'ac5' : True, 'ad5' : True, 'ae5' : True, 'af5' : True, 'ag5'
        : True    }

    # Open a connection to MongoDB using a with statement such that the
    # connection will be closed as soon as we exit the with statement
    with MongoClient(MONGODB_HOST, MONGODB_PORT) as conn:
        # Define which collection we wish to access
        collection = conn[LACdata][projects]
        # Retrieve a result set only with the fields defined in FIELDS
        # and limit the the results to 55000 -- do I need this on this occasion?
        projects = collection.find(projection=FIELDS, limit=55000)
        # Convert projects to a list in a JSON object and return the JSON data
        return json.dumps(list(projects))


if __name__ == "__main__":
    app.run(debug=True)