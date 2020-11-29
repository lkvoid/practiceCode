from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

# dbpath = "../doubantop250.db"
# conn = sqlite3.connect(dbpath)
# c = conn.cursor()
# cusor = c.execute("select * from TOP250 limit 10")
#
# c.close()
# conn.close()


@app.route('/')
def root():
    # return "hello world"
    return render_template("main.html")

@app.route('/main')
def go2main():
    return render_template("main.html")

@app.route('/mark')
def go2mark():
    return render_template("mark.html")

if __name__ == '__main__':
    app.run()
