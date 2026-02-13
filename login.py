from fastapi import FastAPI
from main import app

@app.get('/login')
def login():
  return 0
