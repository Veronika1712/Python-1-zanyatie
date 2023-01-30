x=int(input())
if x>999: 
    print("Введите трехзначное число")
else:
    print(x//100,x//10%10,x%10,sep=', ')
