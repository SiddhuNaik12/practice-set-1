correct_pin=input()
def check_pin(enter_pin):
    if(correct_pin==enter_pin):
        print("ACCESS GRANTED")
        exit()
    else:
        print("wrong pin enter again")
for i in range(3):
    enter_pin=input()
    check_pin(enter_pin)
print("LOCKED")

