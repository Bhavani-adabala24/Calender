date=list(map(int,input("enter a date in(dd-mm-yyyy) format:").split("-")))
Msum=0
l1=[3,1,3,2,3,2,3,3,2,3,2,3]
l2=[3,0,3,2,3,2,3,3,2,3,2,3]
if (date[2]%4==0):
    for i in range (date[1]-1):
        Msum+=l1[i]
else:
    for i in range (date[1]-1):
        Msum+=l2[i]
leap=int((date[2]-1)/4)
Ysum=((leap*2)+((date[2]-1)-leap))
ODD=(date[0]+Msum+Ysum)%7
match ODD:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 0:
        print("Saturday")