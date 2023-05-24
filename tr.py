# from flask import Flask,render_template
# from sqlalchemy import text 
# from database import engine

# app=Flask(__name__)

# with engine.connect() as conn:
#     result = conn.execute(text("select * from d_name"))
#     count=conn.execute(text("select count(id) from d_name"))
#     # print(result.all()) 
#     # print(count.all())  
# count12=count.all()
# count13=count12[0]
# count1=list(count13)
# count2=count1[0]
# print(count2)
# company_name="rama"

# @app.route("/")
# def hello_world():
#   return render_template('tril.html', count2=count2,company=company_name)

# if __name__=="__main__":
#   app.run(host='0.0.0.0',debug=True)

