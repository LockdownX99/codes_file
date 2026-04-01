def main():
  name = ""
  ai = "Sophia "
  print(f"{ai}: Hi There! i'm Sophia,what is your name ? ")
  name = input("You : ")
  print(f"{ai} : Hello {name} ")
  mood = input(f"{ai} : How are you feeling?")
  if "sad" in mood.lower() or "tired" in mood.lower():
    print(f"{ai}i'm sorry to hear that! ")
    story = input(f"{ai} :  let me tell you a joke")
   
#    if "yes" in story.lower() or "yeah" in story.lower() or "yup" in story.lower():
#      print("(200)")
    keywords = ["yes","yeah","yup","tell","ok","okay"]
    if any(word in story.lower() for word in keywords):
      print("200")
      
    else:
      print(f"{ai} : No problem let's talk about somthing else.")
  else:
    print("404")















if __name__=="__main__":
  main()



