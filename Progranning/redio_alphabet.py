dict={
    "A":"Alpha",
    "B":"Bravo",
    "C":"Charlie",
    "D":"Delta",
    "E":"Echo",
    "F":"Foxtrot",
    "G":"Golf",
    "H":"Hotel",
    "I":"India",
    "J":"Juliett",
    "K":"Kilo",
    "L":"Lima",
    "M":"Mike",
    "N":"November",
    "O":"Oscar",
    "P":"Papa",
    "Q":"Quebec",
    "R":"Romeo",
    "S":"Sierra",
    "T":"Tango",
    "U":"Uniform",
    "V":"Victor",
    "W":"Whiskey",
    "X":"X-ray",
    "Y":"Yankee",
    "Z":"Zulu",
}

user = str(input("You: ")).upper().strip()
#print(user)
rchar = ""
for char in user:
    #print(char)
    #print(dict["A"])
    #print(dict[char])
    #result = dict[char]
    #print(result)
    if char in dict:
        rchar +=dict[char]
        rchar +=" "
        
    else:
        rchar+=char
        rchar+=" "
#isspace()

print(rchar) 

#re_dict = {value:key for key, value in dict.items()}

#print(re_dict)     