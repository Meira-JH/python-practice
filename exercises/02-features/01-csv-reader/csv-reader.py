import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r") as csvFile:
    reader = csv.DictReader(csvFile)
    laureatesList = list(reader)

for laureate in laureatesList:
    if laureate['surname'].lower() == "Einstein".lower():
        pprint(laureate)
        break