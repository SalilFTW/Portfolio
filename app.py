
from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    # For local development:
    app.run(host='0.0.0.0', port=5000, debug=True)
