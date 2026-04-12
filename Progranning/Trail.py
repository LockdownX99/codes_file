from textblob import TextBlob
ai = "Sophia"
name = input(f"{ai} : Hi i'm Sophia, What's your name \nYou: ")
user = input(f"{ai} : hello {name}, How are you feeling ? \nYou: ")
blob = TextBlob(user) 
#check sentiment score
# Polarity > 0 means the user is being positive/agreeable
if blob.sentiment.polarity > 0.3:
  #print("The user sounds happy or is agreeing! (200)")
  #print("200")
  user = input(f"{ai} : That's great, so what did you do all day ?\nYou: ")
  blob = TextBlob(user)
 
elif blob.sentiment.polarity < -0.3:
    #print("The user sounds upset or is disagreeing.")
    #print("404")
  user = input(f"{ai} : Sorry to hear that, what happend tell me! \nYou: ")
else:
  print("The user sounds neutral.")
