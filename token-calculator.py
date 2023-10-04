import tiktoken
import re

RANGE = 10

list = []
def init_list():
    for i in range(RANGE):
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

init_list()

print("NORMAL TEXT")
print_tokens(list, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002
# print_tokens(list, "p50k_base") #text-davinci-002, text-davinci-003
# print_tokens(list, "gpt2") #davinci

def remove_closing(string: str) -> str:
    return string.split("Met vriendelijke groet")[0]

cleaned_closing_list = []

for item in list:
    cleaned_closing_list.append(remove_closing(item))

print("\nZONDER GROET")
print_tokens(cleaned_closing_list, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002

def remove_urls(string: str) -> str:
    all_urls = re.findall('(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', string)
    for url in all_urls:
        string = string.replace(url[0]+"://"+url[1]+url[2], "")

    return string

cleaned_urls_list = []

for item in cleaned_closing_list:
    cleaned_urls_list.append(remove_urls(item))

print("\nZONDER GROET EN ZONDER URLS")
print_tokens(cleaned_urls_list, "cl100k_base") #gpt-4, gpt-3.5-turbo, text-embedding-ada-002

for i in range(RANGE):
    with open("cleaned/" + str(i + 1) + ".txt", "w") as file:
        file.write(cleaned_urls_list[i] + "\n")