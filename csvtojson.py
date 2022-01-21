import csv, json

csvFilePath = {"where your csv file actually is"}
jsonFilePath = {"where your json file actually is"}

#reading csv data and adding data to dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        object_id = csvRow['however you want this sorted']
        data[object_id] = csvRow

#write to json file
with open('jsonFilePath', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
