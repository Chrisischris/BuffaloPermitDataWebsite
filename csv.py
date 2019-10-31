# This function takes an array of keys and values and returns a dictionary.
def makeDictionary(keys, values):
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict


# This function takes a CSV filename and return a list of dictionaries
def readDataFromCSVFile(filename):
    list = []
    f = open(filename, newline='', encoding="utf-8")
    data = f.read().splitlines()
    headers = data[0].split(',')
    for i in range(1, len(data)):
        dict = {}
        lineData = data[i].split(',')
        for x in range(len(headers)):
            dict[headers[x]] = lineData[x]
        list.append(dict)
    return list


# Takes a list of keys and a dictionary, returns a list containing the values of the given keys in that order
def dictionaryToListOfValues(keys, dict):
    list = []
    for key in keys:
        list.append(dict.get(key))
    return list


# Writes a list of dictonaries to a CSV file
def writeDataToCSVFile(filename, dicts, keys, writeHeader):
    f = open(filename, "w")
    if(writeHeader):
        for i in range(len(keys)):
            if (i < len(keys) - 1):
                f.write(keys[i] + ', ')
            else:
                f.write(keys[i])
        f.write('\n')

    for dict in dicts:
        for i in range(len(keys)):
            if (i < len(keys) - 1):
                f.write(dict.get(keys[i]) + ', ')
            else:
                f.write(dict.get(keys[i]))
        f.write('\n')
    f.close()
    return