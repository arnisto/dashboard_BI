from flask import Flask,render_template

from flask_mysqldb import MySQL

import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "bi_project"

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    cur = mysql.connection.cursor()
    data = cur.execute('SELECT Age,Gender FROM cube1')
    if data > 0:
        row_headers=['x','y']
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            res = tuple((int(result[0]), int(result[1])))
            json_data.append(dict(zip(row_headers,res)))

        return render_template('index.html',data=json.dumps(json_data))

if __name__=='__main__':
    app.run(debug=True)