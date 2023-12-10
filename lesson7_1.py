import random
import pyinputplus as py
while True:
    min = 1
    max = 180
    randomNum = random.randint(min,max)
    count = 0
    print(randomNum)
    print("=========猜數字遊戲========")    
    while True:
        keyin = py.inputInt(f"猜數字範圍:{min}~{max}:",min=min ,max=max)
        count += 1
        if keyin == randomNum :
            print(F"賓果!猜對了，答案是:{randomNum}")
            break
        elif keyin > randomNum:
            print("數字太大了")
            max = keyin - 1
        else:
             print("數字太小了")
             min =keyin +1
    is_play = py.inputYesNo("您還要繼續玩嗎?(y,n):")  
    if is_play == "no":
          break
    
print(f"遊戲結束，您共猜了{count}次")        

