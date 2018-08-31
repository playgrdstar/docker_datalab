from flask import Flask
from flask import render_template, request
from pymongo import MongoClient

import psycopg2 as pg2
import psycopg2.extras as pgex


app = Flask(__name__, static_url_path='/static')
client = MongoClient('this_mongo')

conn = pg2.connect(host='this_postgres', 
                   user='postgres',
                  database='postgres')

cur = conn.cursor(cursor_factory=pgex.RealDictCursor)


@app.route("/")
def hello():
  return render_template('base.html', title='Data Lab', bodytext='This is the body text')
	# return "You can present and visualise data in this Flask container...."

@app.route("/mongotest")
def mongotest():
    results = client.test_database.country_data.find({'currencies':{'$in':['USD']}})
    results = list(results)
    # count = client.test_database.test_collection.count()
    # return 'Data Count: %d' % count
    return render_template('extension_template.html', title='Mongo Test', results=results)

@app.route("/postgrestest")
def postgrestest():
    cur.execute("""
        SELECT * FROM jupyter_test;
        """)
    result_raw = cur.fetchall()
    # return 'First Result: %s' % result_raw[0]['name']
    return render_template('extension_template.html', title='Postgres Test', results=result_raw[0]['name'])

@app.route("/d3test")
def d3test():
    return render_template('d3_stub.html', title='D3 Test')

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=80)