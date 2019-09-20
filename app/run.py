from app import create_app
app = create_app(config_filename='config.py')
app.run(debug=True)
