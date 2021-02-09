import csv

with open("atestcsv.csv",'r',encoding='utf-8') as f:
    reader=csv.reader(f)
    for row in reader:
        with open("res.csv",'a+',encoding='utf-8',newline='') as fw:
            writer=csv.writer(fw)
            writer.writerow(row)


