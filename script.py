import tiktoken

list = []

with open("aanvraag-1.txt", "r") as file:
    list.append(file.read().replace("\n", " "))

with open("aanvraag-2.txt", "r") as file:
    list.append(file.read().replace("\n", " "))

with open("aanvraag-3.txt", "r") as file:
    list.append(file.read().replace("\n", " "))

with open("aanvraag-4.txt", "r") as file:
    list.append(file.read().replace("\n", " "))

with open("aanvraag-5.txt", "r") as file:
    list.append(file.read().replace("\n", " "))


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def print_tokens(list: list, model: str):
    print("**",model,"**")
    for item in list:
        print("Aanvraag", str(list.index(item)+1) + ":", num_tokens_from_string(item, model), "tokens")
    
    print("\nAverage:", num_tokens_from_string(" ".join(list), model)/len(list),"tokens")
    print("--------------------")

print("NORMAL TEXT")
print_tokens(list, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002
# print_tokens(list, "p50k_base") #text-davinci-002, text-davinci-003
# print_tokens(list, "gpt2") #davinci


def clean(string: str) -> str:
    x  = string.split("Met vriendelijke groet")[0]

    return x

cleanedList = []

for item in list:
    cleanedList.append(clean(item))

print("\nCLEANED TEXT")
print_tokens(cleanedList, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002
# print_tokens(cleanedList, "p50k_base") #text-davinci-002, text-davinci-003
# print_tokens(cleanedList, "gpt2") #davinci