# import requests (to download the page)
import requests

# import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scrape runs)
import time

# Import OS to allow a native notification of the change
import os


def notify(text, title, sound):
    os.system("""osascript -e 'display notification "{}" with title "{}" sound name "{}"'""".format(text, title, sound))


'''
Basso.aiff	Glass.aiff	Purr.aiff
Blow.aiff	Hero.aiff	Sosumi.aiff
Bottle.aiff	Morse.aiff	Submarine.aiff
Frog.aiff	Ping.aiff	Tink.aiff
Funk.aiff	Pop.aiff
'''

while True:

    # Set the url
    url = "https://beta.apple.com/sp/betaprogram/"

    # Download the page
    response = requests.get(url)

    # parse the downloaded page and grab all the texts
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find_all("h2")[0].text == "Coming Soon":

        notify("No Betas yet", "Brace yourselves, Betas are Coming", "Basso.aiff")

        # wait a time (in seconds)
        time.sleep(3600)

        # contine with script
        continue

    else:

        notify("https://beta.apple.com/sp/betaprogram/",
               "Brace yourselves, Betas are here", "Basso.aiff")

        break
