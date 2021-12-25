def max_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(max_num(5,6,1))
print(max_num(1,7,15))

def match_string(str1,str2):
    if str1==str2:
        print("the factory wi explode")
    elif str1>str2:
        print("the football player will win the match")
    else:
        print("you should learn from the first time")

match_string("Mohamed","Farouk")

print("the football is the best solution for us ")


