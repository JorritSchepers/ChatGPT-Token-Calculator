list = []
def init_list():
    for i in range(10):
        with open("aanvraag-" + str(i+1) + ".txt", "r") as file:
            list.append(file.read())

init_list()

keywords = ['Java', '.NET', 'Developer', 'Security', 'Engineer','Informatieanalist','Businessanalist']
blacklist = ['Product owner', 'Manager', 'Tester','Projectleider', 'SharePoint']

def check_for_keywords(list, content: str):
    found_keywords = []
    content_lower = content.lower()
    for item in list:
        if item.lower() in content_lower:
            found_keywords.append(item)
    return found_keywords

for item in list:
    x = check_for_keywords(keywords, item)
    y = check_for_keywords(blacklist, item)
    string = "Misschien relevant"

    if (len(y) > 0):
        string = "Niet relevant"
    elif (len(x) > 0):
        string = "Wel relevant"

    print("\nAanvraag", str(list.index(item)+1) + ":", string)
    print("Keywords:", x)
    print("Blacklist:", y)