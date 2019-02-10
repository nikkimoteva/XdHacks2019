from flask import Flask, render_template, request
import sqlite3 as sql
from PDFOCR import getInformation


app = Flask(__name__, template_folder='webpage')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['GET'])
def addrec():
    try:
        msg = 'test'
        # TODO do the parse logic here
        parsedPDF = getInformation()
        with sql.connect("database.db") as con:
            cur = con.cursor()
            for row in parsedPDF:
                print(row)
                cur.execute("INSERT INTO bloodMD (title, results, range, analysis) VALUES(?, ?, ?, ?)",
                            (row[0], row[1], row[2], row[3])) #TODO add analysis

            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "error in insert operation"

    finally:
        return msg
        con.close()

@app.route('/getdata', methods=['GET'])
def getData():
    msg = 'test'
    try:
        #with sql.connect("database.db") as con:
        rows = getInformation()
            #cur = con.cursor()
            #rows = cur.fetchall()
            #for row in rows:
            #    print(row)
            #print("test")
        print(rows)
        msg = str(rows)
    except:
        msg = "Error displaying information"

    finally:
        return msg
        con.close()

@app.route('/home', methods=['GET'])
def render_static():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)