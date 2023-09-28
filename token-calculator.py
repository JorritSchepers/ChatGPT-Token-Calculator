import tiktoken
import re

list = []
def initList():
    for i in range(10):
        with open("aanvraag-" + str(i+1) + ".txt", "r") as file:
            list.append(file.read())

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def print_tokens(list: list, model: str):
    print("**",model,"**")

    total = 0
    for item in list:
        tokens = num_tokens_from_string(item, model)
        total += tokens
        print("Aanvraag", str(list.index(item)+1) + ":", tokens, "tokens")

    print("\nAverage:", round(total / len(list)),"tokens")
    print("--------------------")

initList()

print("NORMAL TEXT")
print_tokens(list, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002
# print_tokens(list, "p50k_base") #text-davinci-002, text-davinci-003
# print_tokens(list, "gpt2") #davinci

def cleanGroet(string: str) -> str:
    x  = string.split("Met vriendelijke groet")[0]
    return x

cleanedGroetList = []

for item in list:
    cleanedGroetList.append(cleanGroet(item))

print("\nZONDER GROET")
print_tokens(cleanedGroetList, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002

def cleanUrls(string: str) -> str:
    allUrls = re.findall('(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', string)
    for url in allUrls:
        string = string.replace(url[0]+"://"+url[1]+url[2], "")
    return string

cleanedUrlsList = []

for item in cleanedGroetList:
    cleanedUrlsList.append(cleanUrls(item))

print("\nZONDER GROET EN ZONDER URLS")
print_tokens(cleanedUrlsList, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002