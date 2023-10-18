from flask import Flask,render_template,request
import json
with open('data.json','r') as f:data=json.load(f)
drinks,zero,doin=data['drinks'],0.00,''
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def thirstapp():
    def add():
        global zero,doin
        zero+=float(request.form['amount'])
        doin='JUST ADDED '+request.form['amount']+' $ TO THE AVAILABLE'
    def buy():
        global zero,doin
        for drink in drinks:
            if drink['name']==request.form['dd']:
                if drink['price']>zero:
                    doin='JUST TRIED TO BUY '+request.form['dd']+', BUT MONEY NOT ENOUGH. PLEASE ADD SOME!'
                else:
                    zero-=drink['price']
                    doin= 'JUST BOUGHT '+request.form['dd']+' FOR $ '+str(drink['price'])+'. ENJOY!'
    if request.method=='POST':
        clicked=request.form['button']
        if clicked=='ADD':add()
        if clicked=='BUY':buy()
    return render_template('index.html',drinks=drinks,zero=zero,doin=doin)
if __name__=='__main__':app.run(debug=True)