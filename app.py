
from flask import Flask,render_template,request
import math

app=Flask(__name__)
#Homepage
@app.route("/")
def home(): #decorator
    return render_template("home.html")

@app.route("/about")
def about(): #decorator
    return render_template("about.html")


@app.route("/contact")
def contact(): #decorator
     return render_template("contact.html")



@app.route("/form",methods=['GET','POST'])
def form(): 
     result=" "
     if request.method=='GET':
        return render_template("home.html")
     else:
        number1=float(request.form['number1'])
         
        number2=float(request.form['number2'])
        operation =request.form['result']
       
        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1-number2
        elif operation == "/":
              result=(number1/number2)
        elif operation == "*":
             result=(number1*number2)
            
         
     return render_template("home.html",result=result)
if __name__ =="__main__":
    app.run(debug=True) #agar app disturb ho to error ko check kr sakain


