from backend.app import create_app
from backend.src.api import create_api


app = create_app()

if __name__ == '__main__':
    app.run()


