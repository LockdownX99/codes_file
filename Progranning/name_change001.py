japanes = {"a":"কা","b":"তু","c":"মি","d":"টি","e":"কু","f":"লু","g":"জি","h":"রি","i":"মি","j":"জু","k":"কি","l":"ন","m":"মু","n":"টো","o":"রিন","p":"তা","q":"চু","r":"সাই","s":"টু","t":"আরি","u":"ডু","v":"রু","w":"ফু","x":"জি","y":"মেই","z":"না"}
name = str(input("your name"))
name_japanes = ""

for char in name:
    if char in japanes:
        name_japanes += japanes[char]
    else:
        print("invalid!")

print(name_japanes)