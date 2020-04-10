def f():
    fruit = ["Apple","Orange","Pear","Banana","Pineapple"]
    
    guess = input("fruit's name:")

    if guess in fruit:
        print("Bingo!!!")
    else:
        print("Sorry...")


f()
