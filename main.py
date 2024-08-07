import os
from flask import Flask, render_template, request, flash
from openai import OpenAI
import psycopg2
import secrets
from contextlib import closing
import atexit

app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def generate_sql_query(input_text, temper, db_schema):
    prompt = f"""
### Task
Generate a SQL query to answer [QUESTION]{input_text}[/QUESTION]

### Database Schema
The query will run on a database with the following schema:
{db_schema}

### Answer
Given the database schema, here is the SQL query that [QUESTION]{input_text}[/QUESTION]
[SQL]
"""

    system_prompt = f"""
You are a helpful AI assistant expert in querying SQL Database to find answers to user's question.
1. Create and execute a syntactically correct SQL Server query.
2. Limit the results to 10 unless specified otherwise.
3. Order the results by a relevant column to ensure the most interesting examples are returned.
4. Only request specific columns relevant to the query.
5. Not perform any Data Manipulation Language (DML) operations such as INSERT, UPDATE, DELETE, or DROP.
6. Double-check my queries before execution and provide a response based on the query results.
7. If a question doesn't relate to the database, I'll respond with "I don't know".
8. If a question is meaningless or empty, I'll respond with "Meaningless".
"""

    completion = client.chat.completions.create(
        model="model-identifier",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=temper,
    )

    return completion.choices[0].message.content

def connect_to_postgresql(username, password, host, database):
    try:
        connection = psycopg2.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        return connection
    except Exception as e:
        print("Error connecting to PostgreSQL:", e)
        return None

def execute_psql_query(connection, query):
    try:
        with closing(connection.cursor()) as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except Exception as e:
        flash("Query execution was unsuccessful! Check the query properly!")
        flash(e)
        return None

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user_text = request.form.get('user_text', '') 
        temper = request.form.get('temperature', '')
        db_schema = request.form.get('db_schema', '')
        sql_query = generate_sql_query(user_text, temper, db_schema)
        return render_template('index.html', sql_query=sql_query, user_text=user_text)
    else:
        return render_template('index.html')

@app.route('/execute_query', methods=['POST'])
def execute_query():
    query = request.form['query']
    user_name = request.form.get('user_name', '')
    password = request.form.get('password', '')
    host = request.form.get('host', '')
    database = request.form.get('database', '')
    feedback = request.form.get('feedback_score', '')
    connection = connect_to_postgresql(user_name, password, host, database)

    results = execute_psql_query(connection, query)

    if results:
        flash("Query executed successfully!")
        return render_template('index.html', output_tuples=results)
    else:
        return render_template('index.html', sql_query=query, output_tuples=None)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='127.0.0.1', port=port, debug=True)
