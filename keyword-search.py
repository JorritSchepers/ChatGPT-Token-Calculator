list = []
def initList():
    for i in range(10):
        with open("aanvraag-" + str(i+1) + ".txt", "r") as file:
            list.append(file.read())

initList()

keywords = ['Java', '.NET', 'Developer', 'Security', 'Engineer','Informatieanalist','Businessanalist']
blacklist = ['Product owner', 'Manager', 'Tester','Projectleider', 'SharePoint']

def checkForBlacklist(string: str) -> list:
    foundBLwords = []
    for bw in blacklist:
        if bw.lower() in string.lower():
            foundBLwords.append(bw)
    return foundBLwords

def checkForKeywords(string: str) -> list:
    foundKeywords = []
    for item in keywords:
        if item.lower() in string.lower():
            foundKeywords.append(item)
    return foundKeywords

for item in list:
    x = checkForKeywords(item)
    y = checkForBlacklist(item)
    string = "Misschien relevant"

    if (len(y) > 0):
        string = "Niet relevant"
    else:
        if (len(x) > 0):
            string = "Wel relevant"

    print("\nAanvraag", str(list.index(item)+1) + ":", string)
    print("Keywords:", x)
    print("Blacklist:", y)