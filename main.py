import PyPDF2
import data_func
import csv

reader = PyPDF2.PdfFileReader('War_and_Peace_NT.pdf')

print(reader.documentInfo)

num_of_pages = reader.numPages 
print('Number of pages: ' + str(num_of_pages))