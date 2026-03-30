japanes = {"a":"ka",
"b":"tu","c":"mi","d":"tti",
"e":"ku","f":"lu","g":"ji",
"h":"ri","i":"mi","j":"ju",
"k":"ki","l":"n","m":"mu",
"n":"tto","o":"rin","p":"ta",
"q":"chu","r":"sai","s":"ttu",
"t":"ari","u":"du","v":"ru",
"w":"fu","x":"ji","y":"mei",
"z":"na"
}
name = str(input("your name "))
name_japanes = ""

for char in name:
    if char in japanes:
        name_japanes += japanes[char]
    else:
        print("invalid!")

print(name_japanes)
