from flask import Flask, render_template,request

app  = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST","GET"])
def result():
    if request.method == "GET":
        return "PLZ Enter MARKS"
    else:
     phy = request.form.get("phy")
     cal = request.form.get("cal")
     isl = request.form.get("isl")
     return render_template("result.html" , phy = phy, cal = cal, isl = isl)




if __name__ == "__main__":
    app.run(debug=True) 
       
     
