# Load CSV Using Python Standard Library
#import csv
from csv import reader
import numpy

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())


# Load pima-indians-diabetes dataset
filename = 'pima-indians-diabetes.data.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
print(dataset[0])
# convert string columns to float
for i in range(len(dataset[0])):
  str_column_to_float(dataset, i)
print(dataset[0])
