from sqlalchemy import create_engine,text 

db_string= "mysql+pymysql://1b3sypay1d7f1zlj2jkr:pscale_pw_xNJnW3Qzg40GJFBd5S1f02oG6ytxGNQ5Ym9zXFfXioY@aws.connect.psdb.cloud/akshaya?charset=utf8mb4"
engine = create_engine(
    db_string,
    connect_args={
        "ssl": {
            "ca": r"C:\Users\K NONIESH REDDY\OneDrive\Desktop\dbms phase2\test\cacert.pem"
        }
    }
   )

# with engine.connect() as conn:
#     result=conn.execute(text("select * from d_name")) 
#     # print(result.all())
#     count=conn.execute(text("select count(id) from d_name"))
#     for i in count.all():
#         x=list(i) 
#         y=x[0]
#         print(y)
