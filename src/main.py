from os import getenv

from src.server import create_server


def main():
    server = create_server(__name__)
    port = int(getenv('PORT', '3000'))
    server.run(debug=True, port=port, host='0.0.0.0', load_dotenv=False)
