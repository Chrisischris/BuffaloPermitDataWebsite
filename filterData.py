# This function must return a list of all the dictionaries from the input list which contain the indicated key:value pairing.
def filterIn(data, key, value):
    list = []
    for dict in data:
        if(dict.get(key) == value):
            list.append(dict)
    return list

# This function must return a list of all the dictionaries from the input list which do NOT contain the indicated key:value pairing.
def filterOut(data, key, value):
    list = []
    for dict in data:
        if(dict.get(key) != value):
            list.append(dict)
    return list

# This function must return a list of all the dictionaries from the input list which contain the key:value pairs where low <= value < high.
def filterInRange(data, key, low, high):
    list = []
    for dict in data:
        if(int(float(dict.get(key))) >= low and int(float(dict.get(key))) < high):
            list.append(dict)
    return list

# This function must return a list of all the dictionaries from the input list whose 'issued' date is in the indicated month.
def filterByMonth(data, month):
    list = []
    for dict in data:
        date = dict.get(' issued')
        m = int(date[6:8])
        if(month == m):
            list.append(dict)
    return list

# This function must return a list of all the dictionaries from the input list whose 'issued' date is in the indicated year.
def filterByYear(data, year):
    list = []
    for dict in data:
        date = dict.get(' issued')
        y = int(date[1:5])
        if(year == y):
            list.append(dict)
    return list