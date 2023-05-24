from sqlalchemy import create_engine,text 

db_string= "mysql+pymysql://y8y6kea6vzlxxebwqe3d:pscale_pw_5TH4OmawQQ5fxL9xSGEU5nPYjY95ihAUlYStCQ1EwP0@aws.connect.psdb.cloud/akshaya?charset=utf8mb4"
engine = create_engine(
    db_string,
    connect_args={
        "ssl": {
            "ca": r"C:\Users\K NONIESH REDDY\OneDrive\Desktop\dbms phase2\test\cacert.pem"
        }
    }
   )

with engine.connect() as conn:
    result=conn.execute(text("select * from d_name")) 
    # print(result.all())
    count=conn.execute(text("select count(id) from d_name"))
    for i in count.all():
        x=list(i) 
        y=x[0]
        print(y)
  