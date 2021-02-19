from bs4 import BeautifulSoup
import requests


FILTERATTRIBUTE = "data-stat"
MINYEARPAIR = "year_min"
MAXYEARPAIR = "year_max"
PLAYERPAIR = "player"
POSITIONPAIR = "pos"
CAREERSTATSVAL = "Career"
STATSPAIR = "season"


def soupify(soupify_link):
    webpage_request = requests.get(soupify_link)
    webpage = BeautifulSoup(webpage_request.content, "html.parser")
    return webpage


#will add more parameters later
def filter(row, min_year, excludedPos, min_range):
    add_to_list = True
    for col in row.children: #while loop is more efficient, change later
            #FILTERATTRIBUTE is an attribute in every column so do not need to check if it an attribute of the column
        if(col[FILTERATTRIBUTE] == POSITIONPAIR):
            position = col.string
        elif(col[FILTERATTRIBUTE] == MINYEARPAIR):
            player_start_year = int(col.string)
        elif(col[FILTERATTRIBUTE] == MAXYEARPAIR):
            player_end_year = int(col.string)
    if (excludedPos in position or player_start_year < min_year or (player_end_year - player_start_year) <= min_range):
        add_to_list = False


    return add_to_list

#takes in a webpage that has a bunch of links to players in a table
#returns a list of player webpages who played after a specified year and play a certain position
#default values are if filter not wanted
def filter_players(link, min_year = 0, position = "", min_range = 0):
    filtered_years = []
    alphabet_webpage = soupify(link)
    table_body = alphabet_webpage.find("tbody")
    for row in table_body.find_all('tr'):
        if(filter(row, min_year, position, min_range)):
            filtered_years.append(row.find("a")["href"]) #hardcoded

    return filtered_years



#takes in a link to a page with the actual player's stats and a list of stats wanted 
#returns the specified stats as the player's career avg
def extract_stats(link, stats):
    exact_stats = []
    stats_page = soupify(link)
    table_foot = stats_page.find("tfoot") #hardcoded make a generalized method to unhardcode this stuff
    row_data = table_foot.find("tr")
    for col in row_data:
        if(col[FILTERATTRIBUTE] in stats and col.string is not None):
            exact_stats.append(float(col.string))

    return exact_stats






        

        

