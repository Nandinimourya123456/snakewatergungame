import random
print("______________________________________________________ SNAKE WATER GUN GAME_____________________________________________________________ \n")

print("<==u know about  This important game(**snake water gun)game ===>\n \n1.step0 for snake=>snake\n2.step1 for water=>water\n3.step2 for gun=>gun\n")

user=int(input("enter the user number=>")) 
def greaternumber():
   if user>3:
      print("greter then the number ")
greaternumber()


def check( computer,user):
 
    #both of same  computer and user **draw the game
    if  computer==user:    
        return 0 


     #win  computer lose user
    if  computer==0 and user==1:   
       return -1



    #win  computer lose user
    if  computer==1 and user==2:   
       return -1
        
    #win  computer and lose user
    if  computer==2 and user ==0: 
       return -1



    return 1 # this means all time winner the user and lose the  computer    




def all():
   if user<=2: 
    computer=random.randint(0,2)   
    score=check( computer,user)
    print('computer press zero =>', computer)
   if score==0:
    print(" \nits DRAW the game \n")
    print("press the same of number ")
   elif score==1:
    print("you  loss the game ")
  
   elif score>3:
    print("greates")
  
   else:
    print("you won the game ")  
    print("CONGRATULATION!!!")      



all()









