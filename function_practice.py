def hello():
    print("Greetings user")

def pack(pizza, meatballs, spaghetti):
    return[pizza, meatballs, spaghetti]
    

def eat_lunch():
    lunch = []
    if len(lunch) == 0:
        print("my lunchbox is empty")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First i eat {lunch[0]}")
            else:
                print(f"Next i eat {lunch[i]}")

hello()
print(pack("spaghetti", "meatballs", "pizza"))
eat_lunch([])
eat_lunch(["corn", "salsa", "tortilla"])