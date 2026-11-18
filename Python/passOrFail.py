# marks=int(input("Enter your mark: "))
# if marks>= 80:
#     print("you got dist")
# elif marks>=60:
#     print("you got first division")
# elif marks>=40:
#     print("you got 2nd divison")
# else:
#     print("you are fail")            

marks=int(input("Enter your mark: "))
if marks>= 80:
    if marks>100:
        print("Invalid marks")
    else:
        print("you got dist")    
elif marks>=60:
    print("you got first division")
elif marks>=40:
    print("you got 2nd divison")
else:
    print("you are fail")            



