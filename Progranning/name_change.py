#a = ka b = tu c = mi d = ti e = ku f = lu g = ji h = ri i = mi  j = ju  k = ki  l = n  m = mo n = to o = rin p = ta q = chu r = sai s = ttu t = ari u = du v = ru w = fu  x = ji y = mei z = na 
japanes = {"a":"ka","b":"tu","c":"mi","d":"ti","e":"ku","f":"lu","g":"ji","h":"ri","i":"mi","j":"ju","k":"ki","l":"no","m":"mo","n":"to","o":"rin","p":"ta","q":"chu","r":"sai","s":"ttu","t":"ari","u":"du","v":"ru","w":"fu","x":"ji","y":"mei","z":"na"}
name = str(input("your name"))
name_japanes = ""
#sname = list(name)

#print(japanes["a"])

#name = "Sophia"
#for char in name:
    #print(char.upper()) 
#output S,O,P,H,I,A
#////////
#name = "Sophia"
#characters = list(name)
#print(characters)
#//////////////////////////
#fruits = ['apple', 'banana', 'cherry']
#print('banana' in fruits)  # Outputs: True
#print('grape' in fruits)   # Outputs: False

#sentence = "The quick brown fox"
#print("quick" in sentence) # Outputs: True
#a = [1, 2]
#b = [1, 2]
#c = a
#print(a == b) # Outputs: True (values are equal)
#print(a is b) # Outputs: False (different objects in memory)
#print(a is c) # Outputs: True (same object in memory)
#it's search through every characters in user input
for char in name.lower():
    #print(char)
    if char in japanes:
        #print(japanes[char])
        name_japanes += japanes[char]
    else:
        print("invalid")

print(name_japanes)
    


