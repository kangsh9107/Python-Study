# MySQL 라이브러리 임포트
import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='hong', password='1111', db='mydb', charset='utf8')

# Connection 으로부터 Cursor 생성
# curs = conn.cursor()
# curs = conn.cursor(pymysql.cursors.DictCursor) # 컬럼명으로 커서 사용 가능

# SQL문 실행
# sql = "select * from board"
# curs.execute(sql)

# 데이터 Fetch
# rows = curs.fetchall() # 커서에 있는 모든 데이터를 가져옴
# rows = curs.fetchone() # 커서에 있는 값을 하나씩 가져옴
# rows = curs.fetchmany(n) # 커서에 있는 값을 n개씩 가져옴
# curs.rowcount # 커서에 있는 데이터 행 수

# print(rows) # 전체 rows 출력
# print(rows[0]) # 첫번째 row 출력
# for row in rows:
#     print(row['doc'])

# Connection 닫기
# conn.close()

##################################################

# cur = conn.cursor(pymysql.cursors.DictCursor)

# sql = "select * from board where id = %s"
# cur.execute(sql, ('hong'))

# res = cur.fetchall()
# for d in res:
#     print(d['id'])

# 커서 닫기
# cur.close()

# cur = conn.cursor(pymysql.cursors.DictCursor)
# sql = "select * from board where subject like %s or id like %s"
# cur.execute(sql, ('%1%', '%492%'))
# res = cur.fetchall()
# for d in res:
#     print(d['sno'], d['SUBJECT'], d['id'])
# conn.close()

cur = conn.cursor(pymysql.cursors.DictCursor)
sql = """
      insert into board(sno, grp, seq, deep, hit, nal, id, SUBJECT, doc)
      values(getSerial('i'), getSerial(''), 0, 0, 10, now(), %s, %s, %s)
      """
cnt = cur.execute(sql, ('python', 'pymysql로 작성한 제목', '파이썬 간단하네'))
if cnt > 0:
    conn.commit()
    print("success")
else:
    conn.rollback()
    print("fail")
conn.close()