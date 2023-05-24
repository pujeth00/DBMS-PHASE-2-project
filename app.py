from flask import Flask,render_template,request
from sqlalchemy import text 
from database import engine


def no_of_volu():
 with engine.connect() as conn:
    result=conn.execute(text("select * from form")) 
    # print(result.all())
    count=conn.execute(text("select count(id) from form"))
    y=0
    for i in count.all():
        x=list(i) 
        y=x[0]
    return y

app=Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('index.html')
@app.route("/about")
def hello1_world():
  return render_template('about.html')
@app.route("/contact")
def hello2_world():
  return render_template('contact.html')
@app.route("/joinwithus")
def hello3_world():
  num=no_of_volu()
  return render_template('joinwith.html',number=num)
@app.route("/donate")
def hello4_world():
  return render_template('donate.html')
@app.route("/submit" ,methods=['POST','GET'])
def submit():
  first_name1 = request.form.get("fn")
  last_name1 = request.form.get("ln")
  phone_number1=request.form.get("pn")
  email1=request.form.get("em")
  state1=request.form.get("st")
  print(first_name1)
  with engine.connect() as conn:
     query=text("insert into form (first_name,last_name, phone_number, email, state) values (:first_name,:last_name, :phone_number,:email,:state)")
     conn.execute(query,{"first_name":first_name1 , "last_name":last_name1 ,"phone_number":phone_number1,"email":email1,"state":state1})
     conn.commit()
     return "Your data is uploaded in database"

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
