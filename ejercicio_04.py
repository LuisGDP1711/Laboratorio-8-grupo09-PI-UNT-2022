import csv
from tabulate import tabulate
with open("iris.csv", "r") as file:
  reader = csv.reader(file, delimiter=',')

  header = next(reader)

  list = []
  list.append(header)

  for row in reader:
    list.append(row)
  print(tabulate(list, headers="firstrow", tablefmt="fancy_grid", stralign="center", numalign="center"))
