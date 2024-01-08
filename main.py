import requests
from bs4 import BeautifulSoup

url = "https://apps.apple.com/us/app/coinbase-buy-bitcoin-ether/id886427730"

website_html = requests.get(url).text
soup = BeautifulSoup(website_html, 'html.parser')


# Get ranking from app store and parse out ranking of Coinbase in Finance section.
divs = soup.find_all('a', class_='inline-list__item')
new_ranking = divs[0].text
new_ranking = new_ranking.strip().split(" ")
new_ranking = new_ranking[0].split("#")[1]
# print(new_ranking)


file = open("rankings.txt", "a")
file.write(new_ranking + "\n")
file.close()

file = open("rankings.txt", "r")
rankings = file.read()
file.close()

all_rankings = rankings.strip().split("\n")
print(all_rankings) # ["22", "17", "21"]


current_ranking = int(all_rankings[-1])
previous_ranking = int(all_rankings[-2])

delta = current_ranking - previous_ranking

if delta > 0:
  print("increase by", str(delta))
elif delta == 0:
  print("no change, position is", str(current_ranking))
else:
  print("decrease by", str(delta))





# next --> Emails alert rather than prints
# --> cronjobs?


# while True:
#   # code ....
#   time.sleep(60*60*24*7)



# DONE 1. get the html of website.
# DONE 2. pull position + name of item & add to list (BeautifulSoup)
# DONE 3. find coinbase position in list
# DONE 4. save position in txt file
# DONE 5. compare delta
# 6. send email once a week with position + delta
# 7. set cronjob to run it every week



