import random
computer = random.choice([1,-1,0])                              # 1 for stone,-1 for paper,0 for scissors
you = input("Enter your choice(s/p/sc): ")
youdict = {
    "s":1,
    "p":-1,
    "sc":0
}
reversedict = {
    1:"stone",
    -1:"paper",
    0:"scissors"
}
younum = youdict[you]

print(f"You chose {reversedict[younum]}, computer chose {reversedict[computer]} ")

if(computer==-1 and younum==1):
    print("You lose!!!")
elif(computer==-1 and younum==-1):
    print("DRAW!!!")    
elif(computer==-1 and younum==0):
    print("You won!!!") 

elif(computer==0 and younum==1):
    print("You won!!!") 
elif(computer==0 and younum==-1):
    print("You lose!!!") 
elif(computer==0 and younum==0):
    print("DRAW!!!") 
    
elif(computer==1 and younum==1):
    print("DRAW!!!") 
elif(computer==1 and younum==-1):
    print("You won!!!") 
elif(computer==1 and younum==0):
    print("You lose!!!")
else:
    print("Something went wrong!")