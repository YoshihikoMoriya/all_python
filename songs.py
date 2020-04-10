songs = {"1":"Sun",
         "2":"Earth",
         "3":"Moon",
         "4":"Marth",
         "5":"Jupiter"}

n = input("Type a number:")

if n in songs:
        print(songs[n])
else:
        print("sorry...")
