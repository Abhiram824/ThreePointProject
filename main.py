import dataScrape as ds
import trainingModule as tm

PLAYERWEBSITE = "https://www.basketball-reference.com/players/"
GENERALWEBSITE = "https://www.basketball-reference.com/"
ALPHABET = ["a/", "b/", "c/", "d/", "e/", "f/", "g/", "h/", "i/", "j", "k/", "l/", "m/", "n/", "o/", "p/", "q/", "r/", "s/", "t/", "u/", "v/", "w/", "x/", "y/", "z/"]
ds.filter_players(PLAYERWEBSITE + "a/", 2008, "C", 2)