import re
from typing import DefaultDict

if __name__ == "__main__":
    contentFile = "./data/content.txt"
    all_the_text = open(contentFile, 'r', encoding="utf-8").read()
    data = re.findall("\[(.*?)\]",all_the_text, re.I|re.M)
    datalist = []
    for singledata in data:
        singledataList = singledata.split(",")
        for singledataNew in singledataList:
            datalist.append(singledataNew)
    print(datalist)
    datalistSort = sorted(set(datalist),key=datalist.index)
    print(datalistSort)

    datadict = DefaultDict()
    for index in range(len(datalistSort)):
        datadict[datalistSort[index]] = str(index+1)

    print(datadict)

    dataNew = []
    for singledata in data:
        singledataList = singledata.split(",")
        singledataListNew = []
        for singledataNew in singledataList:
            singledataNewConvert = datadict[singledataNew]
            singledataListNew.append(singledataNewConvert)
        print(singledata)
        dataNew.append(",".join(singledataListNew))
    print(dataNew)

    with open("./output/origin.txt", 'w', encoding="utf-8") as f:
        for singledata in data:
            f.write("[" + singledata + "]")
            f.write("\n")
    
    with open("./output/revert.txt", 'w', encoding="utf-8") as f:
        for singledata in dataNew:
            f.write("[" + singledata + "]")
            f.write("\n")

    referenceFile = "./data/reference.txt"
    lines = open(referenceFile, 'r', encoding="utf-8").readlines()
    referenceList = []
    for line in lines:
        # print(line)
        lineList = line.split('	')
        referenceList.append(lineList[-1])
    print(referenceList)

    # print(len(datalistSort))
    referenceListNew = []
    for key in datadict:
        # print(int(key) - 1)
        # print(int(datadict[key])-1)
        try:
            referenceListNew.append(referenceList[int(key) - 1])
        except:
            print(int(key) - 1)
    print(referenceListNew)

    with open("./output/referenceRevert.txt", 'w', encoding="utf-8") as f:
        for singledata in referenceListNew:
            f.write(singledata)
            # f.write("\n")
