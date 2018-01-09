import csv

with open("test.csv", 'rb') as csvfile:
    txt = csvfile.reader(csvfile)
    print txt
    for item in txt:
        print item
