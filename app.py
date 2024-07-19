from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('login.html')

database={'Admin':'123','pavithran':'pavi123','student':'student@123'}

@app.route('/form_login',methods=['POST','GET'])

def login():
    if request.method=='POST':
        name1=request.form['username']
        psd=request.form['password']
        if name1 not in database:
            return render_template('login.html',info='Invalid username')
        else:
            if database[name1]!=psd:
               return render_template('login.html',info='Invalid password')
            else:
               return render_template('home.html',name=name1)
    return render_template('login.html')
if __name__=='__main__':
   app.run(debug=True)