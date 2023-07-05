import sys

from flask import Flask
import connexion

# Create the Flask application
app = Flask(__name__)


# Create the Connexion app
connexion_app = connexion.App(__name__, specification_dir='./swagger/')
app = connexion_app.app

# Add the Swagger definition
# swagger end point http://127.0.0.1:8080/ui/
connexion_app.add_api('swagger.yaml', options={'swagger_url': '/ui/', 'ui_version': 3})

# Run the Flask app
if __name__ == '__main__':
    print("\n --- App started ---", file=sys.stderr)
    app.run(port=8080)

