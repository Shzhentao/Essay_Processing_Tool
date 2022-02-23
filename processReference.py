import re
from typing import DefaultDict

if __name__ == "__main__":
    referenceFile = "./data/reference.txt"
    lines = open(referenceFile, 'r', encoding="utf-8").readlines()
    referenceList = []
    for line in lines:
        # print(line)
        lineList = line.split('	')
        referenceList.append(lineList[-1])
    print(referenceList)
