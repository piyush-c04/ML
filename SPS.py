import random

bot = random.randint(1,3)

human = int(input("Enter 1 for Stone : 2 for Paper : 3 for Scissors\n"))
score = 0


if(human == 1):
    print("human:stone")
elif(human == 2):
    print("human:paper")
elif(human == 3):
    print("human:scissors")



if(bot == 1):
    print("bot:stone")
elif(bot == 2):
    print("bot:paper")
elif(bot == 3):
    print("bot:scissors")




if(bot==human):
    print(bot,"\t",human)
    score+=0

elif(bot == 1 and human == 2):
    score+=1

elif(bot == 2 and human == 3):
    score+=1

elif(bot == 3 and human == 1):
    score+=1

else :
    score-=1

print("*********************************")
if(score> 0):
    print("Human wins")
elif score== 0 :
    print("draw")
else:
    print("Human lost")
