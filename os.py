import csv

movies = [["Top Gun", "Risky Business", "Minority Report","おくりびと"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv","w",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for i in movies:
        w.writerow(i)


