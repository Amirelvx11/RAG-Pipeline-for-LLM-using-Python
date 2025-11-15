''' 
# for Runnig this application please first populate the db and then run this command in your terminal
# (make sure that you have installed requirements & python packages
uvicorn main:app --reload --port 8000
'''
from app.api import app
