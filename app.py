from flask import Flask, render_template, request,url_for,redirect,session
import pymongo
import pandas as pd
import numpy as np
import sys
from sklearn import preprocessing
from sklearn import tree
from sklearn.metrics import accuracy_score,precision_score,f1_score, confusion_matrix,recall_score
from sklearn.model_selection import train_test_split

app = Flask(__name__)
client = pymongo.MongoClient('localhost', 27017)
db = client['DecisionSupportSystem']

@app.route('/')
def home():

   if 'Name' not in session:
      print("session not created")
      return render_template('login.html')

   Company_list = []
   for company in db['Companies'].find():
      company_name = company['Company']
      location = company['Location']
      pns = company['PNS']
      eps = company['EPS']
      pbidt = company['PBIDT']
      sna = company['SNA']

      a = 5.569 * float(pns)
      b = 0.014 * float(eps)
      c = 0.03 * float(pbidt)
      d = 0.216 * float(sna)

      Z = -0.826 + a -b +c - d
   
      if Z < 0.5:
         comment = "Do not invest"
      else:
         comment = "Investment Opportunity"
      print(str(Z))

      
      data = {
         "Name": company_name,
         "Location": location,
         "PNS": pns,
         "EPS": eps,
         "PBIDT": pbidt,
         "SNA": sna,
         "PValue": Z,
         "Comment": comment
      }
      print(data)
      Company_list.append(data)
      
   return render_template('Home.html',Company_list = Company_list)

@app.route('/login',methods = ['POST','GET'])
def login():
   if request.method == 'POST':
      print("Posted")
      username = request.form['email']
      password = request.form['password']

      for user in db['Users'].find({"Email":username}):
         if user['Password'] == password:
            print(user['Name'])
            session['Name'] = user['Name']
            session['Surname'] = user['Surname']
            print("rendering main page")
            return redirect(url_for('home'))
         else:
            message = "invalid password"
            return render_template('login.html',message = message)
      return render_template('signup.html')
      
   return render_template('login.html')
@app.route('/Metrics',methods = ['[POST','GET'])
def Metrics():
   return render_template('Metrics.html')

@app.route('/logout')
def logout():	
	session.pop('Name', None)
	session.pop('Surname', None)
	session.pop('message',None)
	print("Sessions successfully deleted")
	return render_template('login.html')

@app.route('/signup',methods = ['POST','GET'])
def signup():
   if request.method == 'POST':
      Email = request.form['email']
      Name = request.form['name']
      Surname = request.form['surname']
      p1 = request.form['password1']
      p2 = request.form['password2']

      if p1 == p2:
         user = {
            "Name": Name,
            "Surname": Surname,
            "Email": Email,
            "Password": p1
         }
         Transaction = db['Users'].insert_one(user)
         print("User successfully added with transaction_id of " + str(Transaction.inserted_id))
         return render_template('login.html')
      else:
         message = "Password mismatch"
         return render_template('signup.html',message = message)

   return render_template('signup.html')

@app.route('/Record',methods = ['POST','GET'])
def Record():
   if request.method == 'POST':
      company = request.form['search']
      Company_list = []
      for company in db['Companies'].find({"Company":company}):
         company_name = company['Company']
         location = company['Location']
         pns = company['PNS']
         eps = company['EPS']
         pbidt = company['PBIDT']
         sna = company['SNA']
         
         a = 5.569 * float(pns)
         b = 0.014 * float(eps)
         c = 0.03 * float(pbidt)
         d = 0.216 * float(sna)
         Z = -0.826 + a -b +c - d
         
         if Z < 0.5:
            comment = "Do not invest"
         else:
            comment = "Investment Opportunity"
         
         print(str(Z))
         data = {
            "Name": company_name,
            "Location": location,
            "PNS": pns,
            "EPS": eps,
            "PBIDT": pbidt,
            "SNA": sna,
            "PValue": Z,
            "Comment": comment
            }
         Company_list.append(data)
         print(data)
      return render_template('Home.html',Company_list = Company_list)

   Companies = []
   for company in db['Companies'].find():
      Companies.append(company)
   return render_template('Record.html',Companies = Companies)

@app.route('/newcourse',methods = ['POST','GET'])
def newcourse():
   if request.method == 'POST':
      company = request.form['Company']
      location = request.form['Location']
      pns = request.form['pns']
      eps = request.form['eps']
      pbidt = request.form['pbidt']
      sna = request.form['sna']


      company = {
         "Company": company,
         "Location": location,
         "PNS": pns,
         "EPS": eps,
         "PBIDT": pbidt,
         "SNA": sna
      }
      
      db['Companies'].insert(company)
      print("Company successfully added")
      return render_template('Home.html')
   return render_template('newcourse.html')

@app.route('/delete')
def delete():
   db['Courses'].delete_many({})
   db['Marks'].delete_many({})
   return render_template('Home.html')

@app.route('/Marks',methods = ['POST','GET'])
def Marks():
   return redirect(url_for('home'))
if __name__ == '__main__':
   app.secret_key = 'super secret key'
   app.config['SESSION_TYPE'] = 'filesystem'
   app.debug = True
   app.run()
   app.run(debug = True)
