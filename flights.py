import csv
from datetime import datetime

# read flights data from original file 
file = open('flights.csv', 'r+', encoding="utf-8")
csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
nSuccess = 0

for row in csvreader:
        arrivalTime = datetime.strptime(row[1].strip(), '%H:%M')
        departureTime = datetime.strptime(row[2].strip(), '%H:%M')

        delta = (departureTime - arrivalTime).total_seconds()/60
        if delta >= 180 and nSuccess < 20:
                row[3] = 'success'
                nSuccess += 1
        else:
                row[3] = 'fail'
        rows.append(row)

# close file
file.close()

# save result in another csv file
with open('flightsUpdated.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(header)
    write.writerows(rows)

