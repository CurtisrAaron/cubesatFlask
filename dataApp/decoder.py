import csv

def dec(data, constant):
    return(data*data*constant[0] + data*constant[1] + constant[2])

class main():
    def __init__(self):
        f = open('/var/www/dataApp/dataApp/csvData.csv')
        csv_f = csv.reader(f)
        f = open("/var/www/dataApp/dataApp/decData.csv","w")

        fieldnames = [  'frame','time','hi','hi',
                                                    'Total Solar', '+x','-x','+y',
                                                    '-y','RF','Clk','Batt Discharge',
                                                    'Batt V','H-Batt V','Batt Charge', 'Batt Temp',
                                                    'Baseplate Temp','PA Temp','+x F','+z F',
                                                    '5a','5b','5c','5d',
                                                    '6a','6b','6c','6d']

        csvfile = csv.DictWriter(f, fieldnames = fieldnames)
        csvfile.writeheader()

        key = [ (0, 29.5, 0),(0, -20, 1970),(0, -20, 1970),(0, -20, 1970),
                (0, -20, 1970),(.0008,-.16, 8),(0, .24, 0),(0, 40, -2000),
                (0, .1, 6.4),(0, .1, 0),(0, .15, 0),(0, -1.48, 95.8),
                (0, -1.48, 95.8),(0, -1.48, 95.8),(0, -1.48, 95.8),(0, -1.48, 95.8),
                (0, -1.48, 95.8),(0, 11.67, 0),(0, -1.48, 95.8),(0, .82, 11),
                (1, 0, 0),(.1, 0, 0),(.01, 0, 0),(0, 1, 0)]


        for row in csv_f:
            for i in range(4,28):
                row[i] = dec(int(row[i][1:3]),key[i-4])
            print(row)
            d = dict(zip(fieldnames,row))
            print(d)
            csvfile.writerow(d)
        f.close()
