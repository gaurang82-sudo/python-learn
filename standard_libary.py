# from pathlib import Path
# from zipfile import ZipFile
# import csv
# import json
# import sqlite3
# from datetime import datetime, timedelta
# import random
# import webbrowser
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib


# path = Path(r"G:\project\python-learn")

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

# path_py = Path(r"G:\project\python-learn\ex1.py")

# print(path_py.exists())
# path_py.rename("int.txt")


# with ZipFile("file.zip", "w") as zip:
#    for pt in path.rglob("*.*"):
#        zip.write(pt)


# with ZipFile(r"G:\movies\Lucifer_s04.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo(
#         "Lucifer.Season.4.S04.720p.NF.Hin-Eng.WEB-DL.x265-KatmovieHD.Eu/Lucifer.S04E02.720p.NF.WEB-DL.x265-KatmovieHD.Eu.mkv")
#     print(info.file_size)
#     print(info.compress_size)


# with open("data.csv",) as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)


# movies = [
#     {"id": 1, "tittle": "terminator", "year": 1989},
#     {"id": 2, "tittle": "herrypotter", "year": 1999},

# ]
# data = json.dumps(movies)
# Path("movies.json").write_text(data)
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies)


# with sqlite3.connect("db.sqlite3") as conn:
#     #command = "INSERT INTO Movies VALUES(?,?,?)"
#     # for movie in movies:
#     #     conn.execute(command, tuple(movie.values()))
#     # conn.commit()
#     command = "SELECT * FROM Movies"
#     cousor = conn.execute(command)
#     # for row in cousor:
#     #     print(row)

#     movies = cousor.fetchall()
#     print(movies)
# dt2 = datetime(2020, 1, 1) + timedelta(1)
# dt1 = datetime.now()
# duratiomn = dt1 - dt2
# print(duratiomn)
# print("days", duratiomn.days)
# print("second", duratiomn.seconds)
# print("total_second", duratiomn.total_seconds())

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(random.choices([1, 2, 4, 3, 9, 6, 7, ], k=2))
# print(random.choices("abcedefghikjlmop", k=4))

# num = [1, 2, 3, 5]
# random.shuffle(num)
# print(num)

# print("Deployment completed")
# webbrowser.open("https://www.google.com")
# message = MIMEMultipart()
# message["from"] = "javiya gaurang"
# message["to"] = "dilipbahijaviya81@gmail.com"
# message["subject"] = "This is a test message"
# message.attach(MIMEText("body"))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("javiyagaurang7@gmail.com", "*********")
#     smtp.send_message(message)
#     print("send ..........................................................................")
