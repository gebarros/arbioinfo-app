from app import create_app
app = create_app(mode='Development')
app.run(debug=True)
