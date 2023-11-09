import csv

filename = "students.csv" # ชื่อไฟล์

# อ่านไฟล์
with open(filename, 'r') as data:
    for line in csv.DictReader(data): # อ่านโดยแปลงเป็น dictionary
        print(line)   
        # id ทั้งหมด
        print("id:", line['id'])
        # fname ทั้งหมด
        print("firstname:",line['fname'])
        # lname ทั้งหมด
        print("lastname:", line['lname'])