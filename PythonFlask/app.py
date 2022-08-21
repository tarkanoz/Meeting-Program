from flask import Flask,render_template,request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",isim="Michael Jackson")



@app.route("/toplam",methods=["GET","POST"])
def toplam():
    if request.method == "POST":
        number1= request.form.get("title")
        number2=request.form.get("director")
        number3=request.form.get("person")
        number4=request.form.get("time")
        number5=request.form.get("timeend")
        return render_template("number.html")
    else :
        return render_template("number.html",number1=number1,number2=number2,number3=number3,number4=number4,number5=number5)
if __name__ =="__main__":
    app.run(debug=True)