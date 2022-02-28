import csv
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow('2020.10.15 - The first item'.split(' - '))
    writer.writerow('5050.10.15 - The second item'.split(' - '))
    writer.writerow('3030.10.15 - The fifth item'.split(' - '))
    writer.writerow('4040.10.15 - The third item'.split(' - '))
