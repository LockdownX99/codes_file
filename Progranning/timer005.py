def main():
  hour()



def hour():
  for hour in range(24):
    #print(hour)
    if (hour % 2 == 0):
      print(f"Hour {hour} machine A is running ")
    elif(hour % 2 == 1):
      print(f"Hour {hour} machine B is running ")
    

if __name__ == "__main__":
  main()