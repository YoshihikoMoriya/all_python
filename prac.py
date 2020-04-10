pop = []  #pop songs list
jazz = [] #jazz songs list

def collect_songs():
    song = "Enter a song:"
    ask = "Type p or j. q to quit"

    while True:
        genre = input(ask)
        if genre == "q":
            break
        if genre == "p":
            p = input(song)
            pop.append(p)
        elif genre == "j":
            j = input(song)
            jazz.append(j)
        else:
            print("Invalid.")

    print("pop songs: ",pop)
    print("jazz songs: ",jazz)

collect_songs()
