

import requests
import selectorlib
import smtplib,ssl
import os
import time
import sqlite3

connection=sqlite3.connect("data1.db")
cursor=connection.cursor()

"INSERT INTO event VALUES('Tiger','Tiger city','2025.01.21')"

URL="https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    response=requests.get(url)
    source=response.text
    return source

def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
    value=extractor.extract(source)['tou']
    return value

def send_email(message):
    host="smtp.gmail.com"
    port=465

    username = "niranjangowda.583@gmail.com"
    password=os.getenv("PASSWORD")

    receiver="niranjangowda.583@gmail.com"
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
    print("email was sent")


def store(add):
    row = add.split(",")
    row = [item.strip() for item in row]
    cursor.execute("insert into event values(?,?,?)",row)
    connection.commit()


def read(read):
    row=read.split(",")
    row=[item.strip() for item in row]
    band,city,date = row
    cursor.execute("select * from event where band=? and city=? and date=?",(band,city,date))
    result = cursor.fetchall()
    print(result)
    return result


if __name__=="__main__":
    while True:
            scrape_result=scrape(URL)
            extract_result=extract(scrape_result)
            print(extract_result)


            if extract_result !="No upcoming tours":
                content = read(extract_result)

                if not content :
                    store(extract_result)
                    send_email(message="hey new event was found")

            time.sleep(2)