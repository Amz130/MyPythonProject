import csv #so I can read the file with CSV reader

#first test read the lines and print them
def ReadTheFile(fileName):
    with open(fileName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
    csvfile.close()


#For first test

ReadTheFile('Data.csv')
