# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:41:38 2023

@author: urmii
"""

import psycopg2 as pg2
conn=pg2.connect(database='dvdrental',user='postgres',password='root')
#establish connection and start cursor to be ready to query
cur=conn.cursor()
#pass in a postgresql query as a string
cur.execute("select * from payment")

cur.fetchone()
cur.fetchmany(10)
cur.fetchall()
conn.close()
cur.execute('''create table cours(courese_id serial primary key,
            courese_name varchar(40) unique not null,
            courese_instru varchar(50) not null,
            topic varchar(60) not null);
''')
conn.commit()
cur.close()

cur.execute("""insert into cours(courese_name,courese_instru,topic)
                values('python','ganesh','theory')""")
cur.execute("""insert into cours(courese_name,courese_instru,topic)
                values('java','mahesh','practical')""")
cur.execute("""insert into cours(courese_name,courese_instru,topic)
                values('C','yogesh','DLL')""")
cur.execute("""insert into cours(courese_name,courese_instru,topic)
                values('C++','kalpesh','ABC')""")
conn.commit()

cur.execute("select * from cours")
data=cur.fetchall()
cur.commit()
for i in data:
    print(i)
    
cur.execute('select courese_instru,count(*) from cours group by courese_instru')
conn.commit()
rows=cur.fetchall()
for i in rows:
    print(i)
    
cur.execute('select * from cours order by courese_instru')
conn.commit()
rows=cur.fetchall()
for i in rows:
    print(i)
    


cur.execute('''create table course_admin2(course_id serial,
            course_duration varchar(40) unique not null,
            course_fee varchar(50) not null,
            foreign key(course_id) references cours(courese_id))''')  
conn.commit()
   
cur.execute("""insert into course_admin2(course_id,course_duration,course_fee)
                values(1,'30days','10000')""")
cur.execute("""insert into course_admin2(course_id,course_duration,course_fee)
                values(2,'40days','40000')""")
cur.execute("""insert into course_admin2(course_id,course_duration,course_fee)
                values(3,'60days','70000')""")
cur.execute("""insert into course_admin2(course_id,course_duration,course_fee)
                values(4,'50days','50032')""") 
conn.commit()               

cur.execute('select * from cours inner join course_admin2 on cours.courese_id=course_admin2.course_id')
conn.commit()
rows=cur.fetchall()
for i in rows:
    print(i)
hjhjhjghghgghiiobbjbjbbghbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj















































































































































































































































