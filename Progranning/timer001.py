def main():
   hour() 





def hour():
    machine = 60 * int(input("how many ?  "))
    print(machine)
    minute = 60
    hour = 24
    time = minute * hour
    count = 0 
    for minutes in range(time):
        
        if minutes % machine == 0:
            count = count +1 
            print(count)



if __name__ == "__main__":
    main()