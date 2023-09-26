def time(d,v):
    return v/d
def speed(d, t):
    return d/t
def dis(v, t):
    return v*t
print("Speed, distance and time calculator")    

while True:
    choice = input("Enter choice(1/2/3): ")

    if choice in ('1', '2', '3'):
        try:
            #timee = float(input("Enter time value: "))
            #distance = float(input("Enter distance value: "))
            f = 0
        except ValueError:
            print("NULL")
            continue

        if choice == '1':
            distance = float(input("Enter distance value: "))
            timee = float(input("Enter time value: "))
            print(speed(distance, timee))

        elif choice == '2':
            speedy = float(input("Enter speed value: "))
            timee = float(input("Enter time value: "))
            print(dis(speedy, timee))

        elif choice == '3':
            distance = int(input("Enter distance value: "))
            speedy = int(input("Enter speed value: "))
            print(time(speedy, distance))
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("LOL")