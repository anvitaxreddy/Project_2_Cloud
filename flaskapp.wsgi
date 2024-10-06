import os
import sys
import logging

# Configure logging
logging.basicConfig(stream=sys.stderr)

# Add the application directory to the system path
sys.path.insert(0, "/var/www/flaskapp")

# Import the Flask app
from app import app as application

# Set a secure secret key
application.secret_key = os.urandom(24)  # Generates a random secret key for each restart
