import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(chars):
    chars=chars.lower()
    if chars in data:
        return data[chars]
    elif chars.title() in data:
        return data[chars.title()]
    elif chars.upper() in data:
        return data[chars.upper()]
    elif len(get_close_matches(chars,data.keys()))>0:
        while True:
            yn= input("Did you mean %s instead?  Y or N: " %get_close_matches(chars,data.keys())[0])
            if yn.upper() == "Y":
                return data[get_close_matches(chars,data.keys())[0]]
            elif yn.upper()=="N":
                return "The word doesn't exist. Please double check it."
            else:
                print("We didn't understand your query.")
    else:
        return "The word doesn't exist. Please double check it."

word=input("Shoot me a word: ")

output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
        print("\n")
else:
    print(output)