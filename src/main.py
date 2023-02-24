from src.server import create_server

def main():
    server = create_server(__name__)

    server.run(debug=True, port=3000)