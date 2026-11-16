import random
Pr =['P' ,'S', 'R']
pr1 = random.choice(Pr)
pr2 = input("اختار P S R: ")
while True :
    if pr1 == pr2:
        print("تعادل")

    elif (pr1 == "R" and pr2 == "S") or (pr1 == "S" and pr2 == "P") or (pr1 == "P" and pr2 == "R"):
        print("pr1 win")

    elif (pr1 == "S" and pr2 == "R") or (pr1 == "P" and pr2 == "S") or (pr1 == "R" and pr2 == "P"):
        print("pr2 win")

    else:
        print("خطأ في الادخال")