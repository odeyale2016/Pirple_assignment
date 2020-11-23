songs={"genre":"Don Jazz", "artist":"Davido Artist", "year": "2020"}
for key in songs:
    print("{0:s}: \"{1:s}\"".format(key.capitalize(), songs[key]))

def guess(key,value):
    return key in songs and songs[key] == value

 


print("\n\nBonus:\n\n")
print("Is the genre of this song \"Don Jazz\"?: {}".format(
    guess("genre", "Don Jazz")))
print("Is the Artist of this song \"Davido Artist\"?: {}".format(
    guess("artist", "Davido Artist")))
print("Is the Year of this song \"2009\"?: {}".format(
    guess("year", "2009")))