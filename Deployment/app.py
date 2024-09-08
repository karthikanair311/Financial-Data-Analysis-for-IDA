from flask import Flask, render_template, send_from_directory, redirect, url_for, request
import pandas as pd
import sqlite3

app = Flask(__name__)

# Database file path
DATABASE = 'financial_data_analysis.db'

@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def run_query():
    # Get the query from the web form
    query = request.form.get('query')
    print(query)
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    try:
        # Execute the query and get the result as a DataFrame
        cur.execute(query)
        query_results = cur.fetchall()
        # Retrieve the column names from the cursor description
        column_names = [description[0] for description in cur.description]
        # Convert query results to a pandas DataFrame
        df = pd.DataFrame(query_results, columns=column_names)
        # Convert the DataFrame to HTML
        result_html = df.to_html(classes='table table-striped', index=False)
    except Exception as e:
        result_html = f"<div class='alert alert-danger'>Error: {e}</div>"
    finally:
        conn.close()
    return render_template('query.html', result_html=result_html)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)    