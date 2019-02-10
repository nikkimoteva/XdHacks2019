import os
import re

from flask import Flask, flash, render_template, request, url_for, redirect, send_from_directory
import sqlite3 as sql
from PDFOCR import getInformation
from werkzeug.utils import secure_filename
from Nutrient import nutrientInit
from GimmeFacts import gimmeFacts

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

    recPotassiumlist = nutrientInit("Potassium", 3)
    recSodiumList = nutrientInit("Sodium", 3)
    recIronList = nutrientInit("Iron", 3)
    recGlucoseList = nutrientInit("Sugar", 3)
    recCalciumList = nutrientInit("Calcium", 3)
    toBePrinted1 = ''
    toBePrinted2 = ''
    toBePrinted3 = ''
    toBePrinted4 = ''
    toBePrinted5 = ''
    toBePrinted6 = ''
    toBePrinted7 = ''
    toBePrinted8 = ''
    toBePrinted9 = ''
    toBePrinted10 = ''
    l = 0
    while l < len(recPotassiumlist[0]):
        if l != len(recPotassiumlist[0]) - 1:
            toBePrinted1 = toBePrinted1 + recPotassiumlist[0][l] + ", "
            toBePrinted2 = toBePrinted2 + recPotassiumlist[1][l] + ", "
            toBePrinted3 = toBePrinted3 + recSodiumList[0][l] + ", "
            toBePrinted4 = toBePrinted4 + recSodiumList[1][l] + ", "
            toBePrinted5 = toBePrinted5 + recIronList[0][l] + ", "
            toBePrinted6 = toBePrinted6 + recIronList[1][l] + ", "
            toBePrinted7 = toBePrinted7 + recGlucoseList[0][l] + ", "
            toBePrinted8 = toBePrinted8 + recGlucoseList[1][l] + ", "
            toBePrinted9 = toBePrinted9 + recCalciumList[0][l] + ", "
            toBePrinted10 = toBePrinted10 + recCalciumList[1][l] + ", "
        else:
            toBePrinted1 = toBePrinted1 + recPotassiumlist[0][l]
            toBePrinted2 = toBePrinted2 + recPotassiumlist[1][l]
            toBePrinted3 = toBePrinted3 + recSodiumList[0][l]
            toBePrinted4 = toBePrinted4 + recSodiumList[1][l]
            toBePrinted5 = toBePrinted5 + recIronList[0][l]
            toBePrinted6 = toBePrinted6 + recIronList[1][l]
            toBePrinted7 = toBePrinted7 + recGlucoseList[0][l]
            toBePrinted8 = toBePrinted8 + recGlucoseList[1][l]
            toBePrinted9 = toBePrinted9 + recCalciumList[0][l]
            toBePrinted10 = toBePrinted10 + recCalciumList[1][l]
        l = l + 1

    recPotassiumList1 = toBePrinted1
    recPotassiumList2 = toBePrinted2

    recSodiumList1 = toBePrinted3
    recSodiumList2 = toBePrinted4

    recIronList1 = toBePrinted5
    recIronList2 = toBePrinted6

    recGlucoseList1 = toBePrinted7
    recGlucoseList2 = toBePrinted8

    recCalciumList1 = toBePrinted9
    recCalciumList2 = toBePrinted10

    if (potassiumLevel > 0):
        potassiumComment = "Your potassium levels seem a bit high! We recommend cutting down on the following foods!"
    elif (potassiumLevel < 0):
        potassiumComment = "Your potassium levels are looking a bit low! We recommend eating some of these foods!"
    else:
        potassiumComment = "Your potassium levels are looking good! Continue eating these foods to keep them healthy!"

    if (sodiumLevel > 0):
        sodiumComment = "Your sodium levels seem a bit high! We recommend cutting down on the following foods!"
    elif (sodiumLevel < 0):
        sodiumComment = "Your sodium levels are looking a bit low! We recommend eating some of these foods!"
    else:
        sodiumComment = "Your sodium levels are looking good! Continue eating these foods to keep them healthy!"

    if (ironLevel > 0):
        ironComment = "Your sodium levels seem a bit high! We recommend cutting down on the following foods!"
    elif (ironLevel < 0):
        ironComment = "Your sodium levels are looking a bit low! We recommend eating some of these foods!"
    else:
        ironComment = "Your sodium levels are looking good! Continue eating these foods to keep them healthy!"

    if (glucoseLevel > 0):
        glucoseComment = "Your sugar levels seem a bit high! We recommend cutting down on the following foods!"
    elif (ironLevel < 0):
        glucoseComment = "Your sugar levels are looking a bit low! We recommend eating some of these foods!"
    else:
        glucoseComment = "Your sugar levels are looking good! Continue eating these foods to keep them healthy!"

    if (calciumLevel > 0):
        calciumComment = "Your calcium levels seem a bit high! We recommend cutting down on the following foods!"
    elif (calciumLevel < 0):
        calciumComment = "Your calcium levels are looking a bit low! We recommend eating some of these foods!"
    else:
        calciumComment = "Your calcium levels are looking good! Continue eating these foods to keep them healthy!"

    # Recommended Range
    potassiumRange = totalInfo[0][2]
    sodiumRange = totalInfo[1][2]
    ironRange = totalInfo[2][2]
    glucoseRange = totalInfo[3][2]
    calciumRange = totalInfo[4][2]

    funFact = gimmeFacts()
    return render_template("summary.html",potassiumLevel=potassiumLevel, sodiumLevel=sodiumLevel, ironLevel=ironLevel, glucoseLevel=glucoseLevel, calciumLevel=calciumLevel, potassiumRange=potassiumRange, sodiumRange=sodiumRange, ironRange=ironRange, glucoseRange=glucoseRange, calciumRange=calciumRange, userCalcium=userCalcium, userGlucose=userGlucose, userIron=userIron, userPotassium=userPotassium, userSodium=userSodium, potassiumComment=potassiumComment, sodiumComment=sodiumComment, ironComment=ironComment, glucoseComment=glucoseComment, calciumComment=calciumComment, recPotassiumList1=recPotassiumList1, recPotassiumList2=recPotassiumList2, recCalciumList1=recCalciumList1, recCalciumList2=recCalciumList2,  recGlucoseList1=recGlucoseList1, recGlucoseList2=recGlucoseList2, recIronList1=recIronList1, recIronList2=recIronList2, recSodiumList1=recSodiumList1, recSodiumList2=recSodiumList2, funFact=funFact)

if __name__ == '__main__':
    app.run(debug=True)