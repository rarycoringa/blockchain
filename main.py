from app.application import app

if __name__ == '__main__':
    # To run this application in development environment,
    # you can run "$ python main.py"
    app.run(host='0.0.0.0', port=8080, debug=True)
