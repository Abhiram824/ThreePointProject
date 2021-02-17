from bs4 import BeautifulSoup
import requests

PLAYERWEBSITE = "https://www.basketball-reference.com/players/"
GENERALWEBSITE = "https://www.basketball-reference.com/"
ALPHABET = ["a/", "b/", "c/", "d/", "e/", "f/", "g/", "h/", "i/", "j", "k/", "l/", "m/", "n/", "o/", "p/", "q/", "r/", "s/", "t/", "u/", "v/", "w/", "x/", "y/", "z/"]
FILTERATTRIBUTE = "data-stat"
MINYEARPAIR = "year_min"
PLAYERPAIR = "player"


def soupify(soupify_link):
    webpage_request = requests.get(soupify_link)
    webpage = BeautifulSoup(webpage_request.content, "html.parser")
    return webpage

#takes in a webpage that has a bunch of links to players in a table
#returns a list of player webpages who played after a specified year
def filter_players_by_years(link, min_year):
    player_link = ""
    filtered_years = []
    alphabet_webpage = soupify(link)
    table_body = alphabet_webpage.find("tbody")
    for row in table_body.find_all('tr'):
        for col in row.children: #while loop is more efficient, change later
            #FILTERATTRIBUTE is an attribute in every column so do not need to check if it an attribute of the column
            if(col[FILTERATTRIBUTE] == PLAYERPAIR):
                link  = col.find("a")["href"]
            elif(col[FILTERATTRIBUTE] == MINYEARPAIR):
                player_start_year = int(col.string)

        if(player_start_year >= min_year):
            filtered_years.append(link)

    return filtered_years

        


        

        

