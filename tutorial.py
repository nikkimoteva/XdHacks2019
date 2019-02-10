import os
from flask import Flask, flash, render_template, request, url_for, redirect, send_from_directory
import sqlite3 as sql
from PDFOCR import getInformation
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__, template_folder='webpage')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route('/summary', methods=['GET'])
def render_summary_static():
    return render_template('summary.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return

@app.route("/test", methods={"POST"})
def test():
    totalInfo = getInformation()

    # User Value
    userPotassium = totalInfo[0][1]
    userSodium = totalInfo[1][1]
    userIron = totalInfo[2][1]
    userGlucose = totalInfo[3][1]
    userCalcium = totalInfo[4][1]

    # User Discrepancy
    potassiumLevel = totalInfo[0][3]
    sodiumLevel = totalInfo[1][3]
    ironLevel = totalInfo[2][3]
    glucoseLevel = totalInfo[3][3]
    calciumLevel = totalInfo[4][3]

    # Recommended Range
    potassiumRange = totalInfo[0][2]
    sodiumRange = totalInfo[1][2]
    ironRange = totalInfo[2][2]
    glucoseRange = totalInfo[3][2]
    calciumRange = totalInfo[4][2]
    return render_template("summary.html",potassiumLevel=potassiumLevel, sodiumLevel=sodiumLevel, ironLevel=ironLevel, glucoseLevel=glucoseLevel, calciumLevel=calciumLevel, potassiumRange=potassiumRange, sodiumRange=sodiumRange, ironRange=ironRange, glucoseRange=glucoseRange, calciumRange=calciumRange, userCalcium=userCalcium, userGlucose=userGlucose, userIron=userIron, userPotassium=userPotassium, userSodium=userSodium)

if __name__ == '__main__':
    app.run(debug=True)