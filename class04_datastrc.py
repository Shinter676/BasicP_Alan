# score = [99,100,23,50]
# sum = 0

# for i in range(len(score)):
    # print(sum)
    # sum += score[i]

# print("total: " ,sum)

# num = [1,2,3,4,5]

# for number in num:
    # if (number % 2 == 0):
        # print("Even : " , number)
    # else:
        # print("Odd :  " , number)

# x = {"name" : "Sun",
    #  "sid":677}


# x ["score"] = 100

# x["name"] = "Tik"

# print(x)

students = [
    {"name": "Nigga","id":11,"score": 85},
    {"name": "Nigga1","id":23,"score": 72},
    {"name": "Nigga2","id":14,"score": 91}
]

for student in students:
    if(student["score"]>90):
        student["score"] = "A"
    elif(student["score"]>80):
        student["score"] = "B"
    elif(student["score"]>70):
        student["score"] = "C"
    else:
        student["score"] = "F"
    print(student)