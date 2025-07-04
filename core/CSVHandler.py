from csv import writer


def updateCSV(file, row_as_list=[]):
    with open(file, 'a', newline='') as mapData:
        w = writer(mapData)
        w.writerow(row_as_list)
        mapData.close()
