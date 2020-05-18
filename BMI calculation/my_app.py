from flask import Flask,request,render_template
import os
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])

def BMI_INDEX():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = request.form.get("weight")
        height = request.form.get('height')
        bmi = round(float(weight)/((float(height)/100)**2),2)

    return render_template("bmi_calc.html",bmi = bmi)

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8000)))