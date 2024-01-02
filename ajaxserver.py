import os
import json
from flask import Flask, redirect, request,render_template, jsonify
import csv
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#created json dictionary
formDetails = {}
...
    
@app.route("/")
def home():
    return render_template('classifiedads.html')

@app.route("/Books.html", methods=["GET"])
def loadBooks():
    if request.method == 'GET':
        print("Loading Books")
        return render_template("Books.html")

@app.route("/BusinessSupplies.html", methods=["GET"])
def loadBS():
    if request.method == 'GET':
        print("Loading BusinessSupplies")
        return render_template("BusinessSupplies.html")

@app.route("/Clothing.html", methods=["GET"])
def loadClothing():
    if request.method == 'GET':
        print("Loading Clothing")
        return render_template("Clothing.html")

@app.route("/Electronics.html", methods=["GET"])
def loadElectronics():
    if request.method == 'GET':
        print("Loading Electronics")
        return render_template("Electronics.html")

@app.route("/Health&Beauty.html", methods=["GET"])
def loadHAndB():
    if request.method == 'GET':
        print("Loading H&B")
        return render_template("Health&Beauty.html")

@app.route("/Home.html", methods=["GET"])
def loadHome():
    if request.method == 'GET':
        print("Loading Home")
        return render_template("Home.html")

@app.route("/Media.html", methods=["GET"])
def loadMedia():
    if request.method == 'GET':
        print("Loading Media")
        return render_template("Media.html")

@app.route("/Moderator Screen.html", methods=["GET","POST"])
def loadMS():
    if request.method == 'GET':
        print("loading MS")
        return render_template("Moderator Screen.html") + json.dumps(formDetails)
    elif request.method == 'POST':
        approve = request.method['approve']
        reject = request.method['reject']
        return render_template('classifiedads.html') + json.dumps(formDetails)
    
        

  #  with open('ex.csv') as f_input, open('Moderator Screen.html', 'w') as f_output:
  #      csv_input = csv.reader(f_input)
 #       header = next(csv_input)    # skip the header
    
    # Write the HTML header
 #   f_output.write("<html>\n<body>\n")
    
 #   for row in csv_input:
  #      f_output.write(f"Current age of Mr. {row[0]} is {row[1]} Years.<br>\n")
        
    # Write the HTML footer
   # f_output.write("</body>\n</html>\n")'

        
    return render_template("Moderator Screen.html") + json.dumps(formDetails)


        
   
    
    # elif request.method == "POST":
    #     fname = request.args.get('fname', None)
    #     return render_template('/', fname=fname)      

    # elif request.method == "POST":
    #     print("sending form")
        
        # if request.method == 'POST':
        #     fname = request.form['fname']
        #     lname = request.form['lname']
        #     email = request.form['email']
        #     descrip = request.form['description']
        #     file = request.form['myFile']
        #     category = request.form['category']

        #     if not(fname in formDetails):
        #         formDetails[email] =  fname, lname, descrip, file, category
        #         print(formDetails)
        #         return json.dumps(formDetails)

@app.route("/form2.html", methods=["POST", "GET"])
def sendForm():
    if request.method == 'GET':
        print("Loading form2")
        return render_template("form2.html")

    elif request.method == "POST":
        print("sending form")
        
        if request.method == 'POST':
            fname = request.form['fname']
            email = request.form['email']
            descrip = request.form['descrip']
            #descrip = request.form['descrip']
            # file = request.form['myFile']
            # category = request.form['category']

            if not(fname in formDetails):
              #  formDetails[fname] =  email, descrip
              formdetails = {
                "fname": fname
                "email": email
                "descrip": descrip
              }
                print(formDetails)
                info = json.dumps(formDetails) #separators=(".","="))
                #theFile = open('ex.csv', 'w')
                #theFile.write(info)
                #theFile.close()
                return render_template("classifiedads.html")
        

        
if __name__ == "__main__":
    app.run(debug=True)