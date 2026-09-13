x=int(input("Enter the number:"))

match x:
    case 1:
        print("sunday\n")
    case  2 :
        print("Monday\n")
    case 3:
        print("Tuesday\n")
    case 4:
        print("Wednesday\n")
    case 5:
        print("Thursday\n")
    case 6:
        print("Friday\n")
    case 7:
        print("Saturday")
    case _:
        print("No more")

