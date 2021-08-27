from backend.app import create_app
from backend.src.api import create_api


app = create_app()
api = create_api()

if __name__ == '__main__':
    app.run()
    api.run(host='0.0.0.1')


