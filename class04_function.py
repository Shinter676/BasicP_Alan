# def hello(name):
    # print("ค่าที่รับเข้ามา" , name)

# name = input("ค่าที่รับ : ")
# hello(name)

#def sum(a, b):
    #total = a + b
    #return total
    

#num1 = int(input("ป้อนตัวเลขตัวที่ 1 : "))
#num2 = int(input("ป้อนตัวเลขตัวที่ 2 : "))
#total = sum(num1, num2)
#print(total)

#def add(num1,num2):
   # result = num1+num2
    #return result

#def main():
    #num1 = int(input("fill 1st : "))
    #num2 = int(input("fill 2st : "))
    #result = add(num1,num2)
    #print("total : " , result)
    
#main()

def add(num1,num2):
    result = num1+num2
    return result

def minus(num1,num2):
    result = num1-num2
    return result

def muti(num1,num2):
    result = num1*num2
    return result

def divi(num1,num2):
    result = num1/num2
    return result

def is_even(num1):
    result = num1 % 2
    if result == 0:
        print("even number : ")
    else:
        print("odd number : ")
        return result


 
def main():
    num1 = int(input("fill first number : "))
    num2 = int(input("fill second number : "))
    print("chosse dam nigga + - * /  ")
    print("[1] + ")
    print("[2] - ")
    print("[3] * ")
    print("[4] / ")
    operation = int(input("เลือกสักอัน : "))
    if (operation == 1):
        result = add(num1,num2)
        print("ผลบวกคือ : " , result)
    elif (operation == 2):
        result = minus(num1,num2)
        print("ผลลบคือ : " , result)
    elif (operation == 3):
        result = muti(num1,num2)
        print("ผลคูณคือ : " , result)
    elif (operation == 4):
        result = divi(num1,num2)
        print("ผลหารคือ : " , result)
 


main()