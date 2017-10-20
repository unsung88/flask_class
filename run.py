from app import app
from sa import sa


sa.init_app(app)

@app.before_first_request
def create_tables():
	sa.create_all()
