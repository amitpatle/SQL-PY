import os
from flask import Flask, request, flash
from openai import OpenAI
import psycopg2
import secrets



app = Flask(__name__)
secret_key = secrets.token_hex(16) 
app.secret_key = secret_key


client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
