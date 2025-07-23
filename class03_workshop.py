Monster = 100
w1 = 60
w2 = 30
w3 = 20
gamestart = True

print("-----------------------------------------------------Link start--------------------------------------------------------")
while gamestart:
    print("[1] Fight or not nigga")
    print("[2] Run away")
    answer = int(input("Answer the damm question: "))
    if answer == 1:
        attackturn = int(input("How many times do you want to hit his ass?: "))
        for i in range(attackturn):
            print("Monster HP:", Monster)
            print("[เลือกอาวุธ : ]")
            print("[Weapon 1]", w1)
            print("[Weapon 2]", w2)
            print("[Weapon 3]", w3)
            weapontype = int(input("เลือกอาวุธ : "))
            if weapontype == 1:
                Monster -= w1
                print("Monster HP:", Monster)
            elif weapontype == 2:
                Monster -= w2
                print("Monster HP:", Monster)
            elif weapontype == 3:
                Monster -= w3
                print("Monster HP:", Monster)
            else:
                print("เลือกดีๆหน่อยน้อง")
            if Monster < 0:
                Monster = 20
            if Monster == 0:
                print("คิริโตะชนะวะ")
                gamestart = False
                break
    elif answer == 2:
        print("You ran away!")
        gamestart = False
    else:
        print("เลือกดีๆหน่อยน้อง")