from fastapi import FastAPI
from main import app

@app.get('/register')
def sign_up():
  return 0
  
