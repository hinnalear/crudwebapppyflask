from flask import Flask, render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = '192.168.1.66'
app.config['MYSQL_USER'] = 'racoon'
app.config['MYSQL_PASSWORD'] = '6OwOYVGE9_7DiAE7'
app.config['MYSQL_DB'] = 'forbiddenfruit'
 
mysql = MySQL(app)

#Creating a connection cursor
# cursor = mysql.connection.cursor()


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT `id`, `login_name`, `full_name`, `passwd`, `email`, `role`, `expire` 
                    FROM `user`''')
    rv = cur.fetchall()
    return str(rv)






if __name__ == '__main__':
    # app.run()
    app.run(debug=True)